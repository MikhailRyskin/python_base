# -*- coding: utf-8 -*-
import random
import logging

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

try:
    import settings
except ImportError:
    exit('Do cp settings.py.default settings.py and set token')


log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    log.addHandler(stream_handler)
    stream_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler(filename='bot.log', encoding='UTF-8')
    file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s', datefmt='%d-%m-%y %H:%M'))
    log.addHandler(file_handler)
    file_handler.setLevel(logging.DEBUG)

    log.setLevel(logging.DEBUG)


class Bot:
    """
    Echo bot для vk.com
    Use Python 3.8
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

    def on_event(self, event):
        """
        Отправляет сообщение назад, если это текст
        :param event: VkBotMessageEvent object
        :return:
        """
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug('отправляем сообщение назад')
            self.api.messages.send(message='это эхо: ' + event.object['message']['text'],
                                   random_id=random.randint(0, 2**20),
                                   peer_id=event.object['message']['peer_id'])
        else:
            log.info('мы пока не умеем обрабатывать такие события %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(settings.GROUP_ID, settings.TOKEN)
    bot.run()
