# -*- coding: utf-8 -*-
import random
from my_token import _token
import vk_api
import vk_api.bot_longpoll


my_group_id = 204336937


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=self.token)
        #  без "from vk_api import bot_longpoll" в  vk_api.bot_longpoll...  bot_longpoll не определяется. Почему?
        #  Разве недостаточно import vk_api?
        #   Нет не достаточно,
        #  делая "import vk_api" вы попадаете в __init__.py пакета "vk_api" где нет ссылки на "bot_longpoll"
        #  А вам нужен модуль, который находится в этом пакете "bot_longpoll"
        #  И нужно указывать  import vk_api.bot_longpoll либо сразу класс from vk_api.bot_longpoll import VkBotLongPoll
        #  Это тоже самое что если бы в прошлом модуле импортировали не "from PIL", а просто "import PIL"
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(vk=self.vk, group_id=self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print('получено событие')
            try:
                self.on_event(event)
            except Exception as exp:
                print(exp)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            # print(event.object)
            #  в видео используют event.object.text и event.object.peer_id, у меня это не работает. Почему?
            # Библиотека за это время немного изменилась и ключи соответственно тоже
            print(event.object['message']['text'])
            self.api.messages.send(message='это эхо:' + event.object['message']['text'],
                                   random_id=random.randint(0, 2**20),
                                   peer_id=event.object['message']['peer_id'])
        else:
            print('мы пока не умеем обрабатывать такие события', event.type)


if __name__ == '__main__':
    bot = Bot(my_group_id, _token)
    bot.run()
