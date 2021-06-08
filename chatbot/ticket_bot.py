# -*- coding: utf-8 -*-
import random
import logging

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from chatbot import ticket_handlers

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


class UserState:
    """ Состояние пользователя внутри сценария."""
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


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
        self.user_states = dict()  # user_id : user state

    def run(self):
        """Запуск бота."""
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

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

        if text == '/ticket':
            self.exit_scenario(user_id)
            text_to_send = self.start_scenario(user_id, 'booking')
        elif text == '/help':
            self.exit_scenario(user_id)
            text_to_send = ticket_settings.HELP_ANSWER
        elif user_id in self.user_states:
            text_to_send = self.continue_scenario(user_id, text)
        else:
            text_to_send = ticket_settings.HELP_ANSWER

        self.api.messages.send(
            message=text_to_send,
            random_id=random.randint(0, 2 ** 20),
            peer_id=user_id
        )

    def start_scenario(self, user_id, scenario_name):
        scenario = ticket_settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)
        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = ticket_settings.SCENARIOS[state.scenario_name]['steps']
        #  continue scenario
        step = steps[state.step_name]
        handler = getattr(ticket_handlers, step['handler'])
        if handler(text=text, context=state.context):
            # next_step
            next_step = step['next_step']
            text_to_send = steps[next_step]['text'].format(**state.context)
            if steps[next_step]['next_step']:
                # switch to next step
                state.step_name = step['next_step']
            else:
                # finish scenario
                log.info('заказан билет: {departure} {destination} {flight} {seats}'.format(**state.context))
                self.user_states.pop(user_id)
        else:
            # retry current step
            text_to_send = step['failure_text'].format(**state.context)
            if state.context['break-scenario']:
                self.user_states.pop(user_id)
        return text_to_send

    def exit_scenario(self, user_id):
        if user_id in self.user_states:
            self.user_states.pop(user_id)


if __name__ == '__main__':
    configure_logging()
    bot = TicketBot(ticket_settings.GROUP_ID, ticket_settings.TOKEN)
    bot.run()
