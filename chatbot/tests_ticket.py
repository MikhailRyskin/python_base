from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock

from pony.orm import db_session, rollback
from vk_api.bot_longpoll import VkBotMessageEvent

from chatbot.generate_ticket import generate_ticket
from ticket_bot import TicketBot
from chatbot import intents


def isolate_db(test_func):
    def wrapper(*args, **kwargs):
        with db_session:
            test_func(*args, **kwargs)
            rollback()
    return wrapper


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
        with patch('ticket_bot.vk_api.VkApi'), patch('ticket_bot.VkBotLongPoll', return_value=long_poller_listen_mock):
            bot = TicketBot('', '')
            bot.on_event = Mock()
            bot.send_image = Mock()
            bot.run()

            bot.on_event.assert_called()
            bot.on_event.assert_any_call(obj)
            assert bot.on_event.call_count == count

    INPUTS = [
        'Привет',
        '/ticket',
        'Москв',
        'париже',
        '12.08.2021',
        '21-06-2021',
        '3',
        '2',
        'очень нужны билеты',
        'да',
        '9217777777',
    ]
    EXPECTED_OUTPUTS = [
        intents.HELP_ANSWER,
        intents.SCENARIOS['booking']['steps']['step1']['text'],
        intents.SCENARIOS['booking']['steps']['step2']['text'],
        intents.SCENARIOS['booking']['steps']['step3']['text'],
        intents.SCENARIOS['booking']['steps']['step3']['failure_text'],
        intents.SCENARIOS['booking']['steps']['step4']['text'].format(
            flights5='1. 21-06-2021 20-40 мп02\n2. 23-06-2021 12-15 мп03\n3. 23-06-2021 18-20 мп04\n'
                     '4. 23-06-2021 23-20 мп05\n5. 24-06-2021 07-20 мп06\n'),
        intents.SCENARIOS['booking']['steps']['step5']['text'],
        intents.SCENARIOS['booking']['steps']['step6']['text'],
        intents.SCENARIOS['booking']['steps']['step7']['text'].format(departure='москва', destination='париж',
                                                                      flight='23-06-2021 18-20 мп04', seats='2',
                                                                      comment='очень нужны билеты'),
        intents.SCENARIOS['booking']['steps']['step8']['text'],
        intents.SCENARIOS['booking']['steps']['step9']['text'].format(phone='9217777777'),
    ]

    @isolate_db
    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['message']['text'] = input_text
            events.append(VkBotMessageEvent(event))

        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('ticket_bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = TicketBot('', '')
            bot.api = api_mock
            bot.send_image = Mock()
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        assert real_outputs == self.EXPECTED_OUTPUTS

    def test_image_generation(self):
        with open('files/ava.jpg', 'rb') as avatar_file:
            avatar_mock = Mock()
            avatar_mock.content = avatar_file.read()

        with patch('requests.get', return_value=avatar_mock):
            ticket_file = generate_ticket('Лондон', 'Брюгге', '23-06-2021 18-20 мп04', '4')

        with open('files/ticket_example.png', 'rb') as expected_file:
            expected_bytes = expected_file.read()

        assert ticket_file.read() == expected_bytes
