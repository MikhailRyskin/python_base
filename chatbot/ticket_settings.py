GROUP_ID = 204336937
TOKEN = '6e69abbb52bce4c7a624adb81b8349b33bc4e39c60a3e5c555eda7e2e135705032cf4eed3f31654f58aec'


HELP_ANSWER = 'Это справка о том, что нужно сделать'

INTENTS = [
    {
        'name': 'Справка',
        'tokens': ('/help'),
        'scenario': None,
        'answer': HELP_ANSWER
    },
    {
        'name': 'Заказ билетов',
        'tokens': ('/ticket'),
        'scenario': 'booking',
        'answer': None
    }
]

SCENARIOS = {
    'booking': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Введите город отправления',
                'failure_text': 'Из этого города нет рейсов. Попробуйте ввести другой город',
                'handler': 'handle_departure',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введите город назначения',
                'failure_text': 'В этот город нет рейсов. Попробуйте ввести другой город',
                'handler': 'handle_destination',
                'next_step': 'step8'
            },
            'step8': {
                'text': 'Введите номер телефона для связи',
                'failure_text': 'Неверный формат номера телефона. Попробуйте ещё раз',
                'handler': 'handle_phone',
                'next_step': 'step9'
            },
            'step9': {
                'text': 'Спасибо за заказ. Мы свяжемся с Вами по номеру {phone} в ближайшее время',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }

    }
}


