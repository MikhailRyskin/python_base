# -*- coding: utf-8 -*-
import random
import logging

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from pony.orm import db_session

from chatbot import ticket_handlers, intents
from models import UserState, TicketInfo

try:
    import ticket_settings
except ImportError:
    exit('Do cp settings.py.default settings.py and set token')


log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    log.addHandler(stream_handler)
    stream_handler.setLevel(logging.ERROR)

    file_handler = logging.FileHandler(filename='bot.log', encoding='UTF-8')
    file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%y %H:%M'))
    log.addHandler(file_handler)
    file_handler.setLevel(logging.DEBUG)

    log.setLevel(logging.DEBUG)


class TicketBot:
    """
    Bot заказа билетов для vk.com
    Use Python 3.8
    поддерживает запрос помощи и сценарий запроса билетов:
    -запрос места отправления
    -запрос места прибытия
    -запрос даты
    -выдача 5 ближайших рейсов и запрос выбора рейса из них
    -запрос количества билетов
    -возможный комментарий
    -запрос подтверждение введённых данных
    -запрос номера телефона
    -сообщение об успешном заказе
    Если шаг не пройден, новый запрос до успешного прохождения
    """
    def __init__(self, group_id, token):
        """
        :param group_id: group id из группы в vk
        :param token: секретный токен группы в vk
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        """Запуск бота."""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

    @db_session
    def on_event(self, event):
        """
        Отправляет сообщение в ответ на ввод пользователя в соответствии со сценарием
        :param event: VkBotMessageEvent object
        :return:
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.info('мы пока не умеем обрабатывать такие события %s', event.type)
            return
        user_id = event.object['message']['peer_id']
        text = event.object['message']['text']
        text = text.lower()
        state = UserState.get(user_id=str(user_id))
        if text == '/ticket':
            self.exit_scenario(state)
            self.start_scenario(user_id, 'booking', text)
        elif text == '/help':
            self.exit_scenario(state)
            self.send_text(intents.HELP_ANSWER, user_id)
        elif state is not None:
            self.continue_scenario(text, state, user_id)
        else:
            self.send_text(intents.HELP_ANSWER, user_id)

    def send_image(self, image, user_id):
        upload_url = self.api.photos.getMessagesUploadServer()['upload_url']
        upload_data = requests.post(url=upload_url, files={'photo': ('image.png', image, 'image.png')}).json()
        image_data = self.api.photos.saveMessagesPhoto(**upload_data)

        owner_id = image_data[0]['owner_id']
        media_id = image_data[0]['id']
        attachment = f'photo{owner_id}_{media_id}'

        self.api.messages.send(
            attachment=attachment,
            random_id=random.randint(0, 2 ** 20),
            peer_id=user_id)

    def send_text(self, text_to_send, user_id):
        self.api.messages.send(
            message=text_to_send,
            random_id=random.randint(0, 2 ** 20),
            peer_id=user_id)

    def send_step(self, step, user_id, text, context):
        if 'text' in step:
            self.send_text(step['text'].format(**context), user_id)
        if 'image' in step:
            handler = getattr(ticket_handlers, step['image'])
            image = handler(text, context)
            self.send_image(image, user_id)

    def start_scenario(self, user_id, scenario_name, text):
        scenario = intents.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        self.send_step(step, user_id, text, context={})
        UserState(user_id=str(user_id), scenario_name=scenario_name, step_name=first_step, context={})

    def continue_scenario(self, text, state, user_id):
        steps = intents.SCENARIOS[state.scenario_name]['steps']
        #  continue scenario
        step = steps[state.step_name]
        handler = getattr(ticket_handlers, step['handler'])
        if handler(text=text, context=state.context):
            # next_step
            next_step = steps[step['next_step']]
            self.send_step(next_step, user_id, text, state.context)
            if next_step['next_step']:
                # switch to next step
                state.step_name = step['next_step']
            else:
                # finish scenario
                log.info('заказан билет: {departure} {destination} {flight} {seats}'.format(**state.context))
                TicketInfo(departure=state.context['departure'], destination=state.context['destination'],
                           flight=state.context['flight'], seats=state.context['seats'])
                state.delete()
        else:
            # retry current step
            self.send_text(step['failure_text'].format(**state.context), user_id)
            if state.context['break-scenario']:
                state.delete()

    def exit_scenario(self, state):
        if state is not None:
            state.delete()


if __name__ == '__main__':
    configure_logging()
    bot = TicketBot(ticket_settings.GROUP_ID, ticket_settings.TOKEN)
    bot.run()
