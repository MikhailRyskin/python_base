import random


#  Принято определять в начале модуля
# TODO определил в начале
_hidden_number = []


#  Для генерации числа удобнее использовать random.sample
#  чем в данном случае random.sample лучше random.choice?
#  choice - случайный элемент из существующего набора данных. Ровно то, что нам нужно
#  sample - новый список из случайных компонентов уже существующего списка. Зачем нам здесь список из 1 элемента?
#  TODO "sample" принимает последовательность необязательно список это может быть просто диапазон
#   random.sample(range(1, 4), 2) - выборка двух случайных элементов из последовательности "range"
#   Это намного проще

def get_hidden_number():
    global _hidden_number
    _hidden_number = []
    numbers_to_choose = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    first_digit = random.choice(numbers_to_choose)
    _hidden_number.append(first_digit)
    numbers_to_choose.remove(first_digit)
    numbers_to_choose.append('0')
    for _ in range(3):
        digit = random.choice(numbers_to_choose)
        _hidden_number.append(digit)
        numbers_to_choose.remove(digit)
    # для тестирования!!!
    print('\nТест! Секретное число:', *_hidden_number)


def checking_number(number):
    if len(number) != 4 or not number.isdigit() or number[0] == '0' or len(set(number)) < 4:
        return False
    else:
        return True


def number_bulls_cows(number):
    global _hidden_number
    bulls_cows = {'bulls': 0, 'cows': 0}
    #  range - len это плохой стиль, для индексов всегда стоит использовать "enumerate"
    # for position in range(len(number)):
    #     if number[position] in _hidden_number:
    #         if number[position] == _hidden_number[position]:
    #             bulls_cows['bulls'] += 1
    #         else:
    #             bulls_cows['cows'] += 1
    # TODO исправил
    for position, digit in enumerate(number):
        if digit in _hidden_number:
            if digit == _hidden_number[position]:
                bulls_cows['bulls'] += 1
            else:
                bulls_cows['cows'] += 1
    return bulls_cows
