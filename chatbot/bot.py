# -*- coding: utf-8 -*-
from my_token import _token
import vk_api


my_group_id = 204336937


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token

    def run(self):
        pass


if __name__ == '__main__':
    bot = Bot(my_group_id, _token)
    bot.run()
