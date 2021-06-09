# TODO Пример создания клавиатуры примеры можно взять в документации
#  - https://vk.com/dev/bots_docs_5?f=4.4.+Callback-%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D0%B8
import json


def generate_button(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }

# TODO Немного поколдовав можно сделать клавиатуру с одной кнопкой.
def build_keyboard(text):
    keyboard = {
        "one_time": True,
        "buttons": [
            [generate_button(text, 'positive')],
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    return str(keyboard.decode('utf-8'))
