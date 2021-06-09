RE_CITIES = {'москв': 'москва', 'рим': 'рим', 'лондо': 'лондон', 'пари': 'париж'}
HELP_ANSWER = 'Для начала заказа билетов введите /ticket. Помощь - /help. При этом процедура заказа начнётся заново.'

# INTENTS = [
#     {
#         'name': 'Справка',
#         'tokens': ('/help'),
#         'scenario': None,
#         'answer': HELP_ANSWER
#     },
#     {
#         'name': 'Заказ билетов',
#         'tokens': ('/ticket'),
#         'scenario': 'booking',
#         'answer': None
#     }
# ]

SCENARIOS = {
    'booking': {
        'first_step': 'step1',
        'steps': {
            'step1': {
                'text': 'Введите город отправления.',
                'failure_text': 'Из этого города нет рейсов. Список возможных городов: {cities_list}.',
                'handler': 'handle_departure',
                'next_step': 'step2'
            },
            'step2': {
                'text': 'Введите город назначения.',
                'failure_text': 'В этот город нет рейсов. Начните заказ заново.',
                'handler': 'handle_destination',
                'next_step': 'step3'
            },
            'step3': {
                'text': 'Введите дату полёта в формате дд-мм-гггг.',
                'failure_text': 'Некорректный формат даты или дата меньше текущей.',
                'handler': 'handle_date',
                'next_step': 'step4'
            },
            'step4': {
                'text': 'Выберите рейс из списка по порядковому номеру:\n {flights5}.',
                'failure_text': 'Этого номера нет в списке.',
                'handler': 'handle_flights',
                'next_step': 'step5'
            },
            'step5': {
                'text': 'Введите количество мест (от 1 до 5)',
                'failure_text': 'Неверное количество мест.',
                'handler': 'handle_seats',
                'next_step': 'step6'
            },
            'step6': {
                'text': 'Дополнительные комментарии (или "нет").',
                'failure_text': 'Некорректный комментарий.',
                'handler': 'handle_comment',
                'next_step': 'step7'
            },
            'step7': {
                'text': 'Подтвердите заказ:\nоткуда: {departure} куда: {destination} дата и рейс: {flight} '
                        'мест: {seats} комментарий: {comment}.\nДля подтверждения введите "да".',
                'failure_text': 'Начните заказ заново.',
                'handler': 'handle_confirm',
                'next_step': 'step8'
            },
            'step8': {
                'text': 'Заказ подтверждён. Введите номер телефона для связи.',
                'failure_text': 'Неверный формат номера телефона. Попробуйте ещё раз.',
                'handler': 'handle_phone',
                'next_step': 'step9'
            },
            'step9': {
                'text': 'Спасибо за заказ. Мы свяжемся с Вами по номеру {phone} в ближайшее время.',
                'failure_text': None,
                'handler': None,
                'next_step': None
            }
        }

    }
}
