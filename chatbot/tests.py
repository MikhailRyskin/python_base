from unittest import TestCase
from unittest.mock import patch, Mock, ANY

from vk_api.bot_longpoll import VkBotMessageEvent

from bot import Bot


class Test1(TestCase):
    RAW_EVENT = {'type': 'message_new', 'object': {'message': {'date': 1621236521, 'from_id': 4753058,
                                                               'id': 94, 'out': 0, 'peer_id': 4753058,
                                                               'text': 'привет бот!!!',
                                                               'conversation_message_id': 94, 'fwd_messages': [],
                                                               'important': False, 'random_id': 0,
                                                               'attachments': [], 'is_hidden': False},
                                                   'client_info': {
                                                       'button_actions': ['text', 'vkpay', 'open_app', 'location',
                                                                          'open_link',
                                                                          'callback', 'intent_subscribe',
                                                                          'intent_unsubscribe'],
                                                       'keyboard': True, 'inline_keyboard': True, 'carousel': False,
                                                       'lang_id': 0}},
                 'group_id': 204336937, 'event_id': '5e64924da9b835267578b658349f584b5ed3471e'}

    def test_run(self):
        count = 5
        obj = {'a': 11}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    def test_on_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)

        send_mock = Mock()
        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.message.send = send_mock

                bot.on_event(event)

        send_mock.assert_called_once_with(
            message='это эхо: ' + self.RAW_EVENT['object']['message']['text'],
            random_id=ANY,
            peer_id=self.RAW_EVENT['object']['message']['peer_id']
        )
