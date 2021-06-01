from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock

from vk_api.bot_longpoll import VkBotMessageEvent

from bot import Bot
from chatbot import settings


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
        # Дублировать "with" не нужно используйте перечисление
        with patch('bot.vk_api.VkApi'), patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
            bot = Bot('', '')
            bot.on_event = Mock()
            bot.run()

            bot.on_event.assert_called()
            bot.on_event.assert_any_call(obj)
            assert bot.on_event.call_count == count

    # def test_on_event(self):
    #     #  А остальная логика где потерялась? Также не хватает ожидаемых ответов от бота
    #     #  Сначала создаем моки
    #     #  - send_mock = Mock()
    #     #  - api_mock = Mock()
    #     #  И присваиваем отправки сообщения мок api_mock.messages.send = send_mock
    #     #  .
    #     #  Затем в цикле собираем список ожидаемых ответов и добавляем VkBotMessageEvent(текст)
    #     #  И потом уже создаем мок для long poll, как в тесте выше, а в "return_value" передаем собранный список
    #     #  .
    #     #  Следующий шаг это сделать патч для VkBotLongPoll больше не нужно,
    #     #  и в return_value уже передаем замоканый long poll
    #     #  И внутри уже создаем бота запускаем его и добавляем ожидаемые ответы
    #     #  .
    #     #  И потом делаем сравнения с количество вызовов, и ожидаемы ответы с реальными
    #
    #     # сейчас оба теста проходят. Тест на on_event сделан как показано в видео.
    #     event = VkBotMessageEvent(raw=self.RAW_EVENT)
    #
    #     send_mock = Mock()
    #     with patch('bot.vk_api.VkApi'), patch('bot.VkBotLongPoll'):
    #             bot = Bot('', '')
    #             bot.api = Mock()
    #             bot.api.messages.send = send_mock
    #
    #             bot.on_event(event)
    #
    #     send_mock.assert_called_once_with(
    #         message='это эхо: ' + self.RAW_EVENT['object']['message']['text'],
    #         random_id=ANY,
    #         peer_id=self.RAW_EVENT['object']['message']['peer_id']
    #     )

    INPUTS = [
        'Привет',
        'А когда?',
        'Где будет конференция?',
        'Зарегистрируйте меня',
        'Вениамин',
        'мой адрес mail@email',
        'mail@email.ru',
    ]
    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.INTENTS[1]['answer'],
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step3']['text'].format(name='Вениамин', email='mail@email.ru'),
    ]

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

        with patch('bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot('', '')
            bot.api = api_mock
            bot.run()

        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        assert real_outputs == self.EXPECTED_OUTPUTS
