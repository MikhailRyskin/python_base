GROUP_ID = 204336937
TOKEN = '6e69abbb52bce4c7a624adb81b8349b33bc4e39c60a3e5c555eda7e2e135705032cf4eed3f31654f58aec'
DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='1111',
    host='localhost',
    database='vk_chat_bot'
)


INTENTS = [
    {
        'name': 'Дата проведения',
        'tokens': ('когда', 'сколько', 'дата', 'дату'),
        'scenario': None,
        'answer': 'Конференция состоится 15 мая, регистрация начнётся в 10 утра.'
    },
    {
        'name': 'Место проведения',
        'tokens': ('где', 'место', 'локация', 'адрес', 'метро'),
        'scenario': None,
        'answer': 'Конференция пройдёт в Ленэкспо, В.О., м. "Приморская". '
    },
    {
        'name': 'Регистрация',
        'tokens': ('регист', 'добав'),
        'scenario': 'registration',
        'answer': None
    }
]

SCENARIOS = {
    'registration': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Чтобы зарегистрироваться, введите своё имя.  Оно будет написано на бейдже',
                'failure_text': 'Имя должно состоять из 3-30 букв, цифр, дефиса. Попробуйте ещё раз',
                'handler': 'handle_name',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введите e-mail. Мы отправим на него все данные',
                'failure_text': 'Во введённом адресе ошибка. Попробуйте ещё раз',
                'handler': 'handle_email',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Спасибо за регистрацию, {name}. Мы отправили на {email} билет, распечатайте его',
                'image': 'generate_ticket_handler',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }

    }
}

DEFAULT_ANSWER = 'Не знаю, как на это ответить. '\
                 'Могу сказать, когда и где пройдёт конференция и зарегистрировать Вас. Просто спросите.'
