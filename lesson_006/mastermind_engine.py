import random

_hidden_number = []

#  Для генерации числа удобнее использовать random.sample
#  чем в данном случае random.sample лучше random.choice?
#  choice - случайный элемент из существующего набора данных. Ровно то, что нам нужно
#  sample - новый список из случайных компонентов уже существующего списка. Зачем нам здесь список из 1 элемента?
#  "sample" принимает последовательность необязательно список это может быть просто диапазон
#   random.sample(range(1, 4), 2) - выборка двух случайных элементов из последовательности "range"
#   Это намного проще
# TODO переделал на random.sample


def get_hidden_number():
    global _hidden_number
    _hidden_number = random.sample(range(1, 10), 1)
    numbers_to_choose = list(range(0, 10))
    numbers_to_choose.remove(_hidden_number[0])
    _hidden_number += random.sample(numbers_to_choose, 3)
    # для тестирования!!!
    print('\nТест! Секретное число:', *_hidden_number)


def number_bulls_cows(number):
    global _hidden_number
    bulls_cows = {'bulls': 0, 'cows': 0}
    for position, digit in enumerate(number):
        if digit in _hidden_number:
            if digit == _hidden_number[position]:
                bulls_cows['bulls'] += 1
            else:
                bulls_cows['cows'] += 1
    return bulls_cows
