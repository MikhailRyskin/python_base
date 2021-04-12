# -*- coding: utf-8 -*-

# Есть функция генерации списка простых чисел

# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
#
# print(get_prime_numbers(20))

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых объектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        # Имена лучше давать осмысленные
        #  например - self.start и self.end
        self.end = n
        self.start = 0
        self.prime_numbers = []

    def __iter__(self):
        self.start = 1
        return self

    def __next__(self):
        while True:
            self.start += 1
            if self.start > self.end:
                raise StopIteration()
            else:
                for prime in self.prime_numbers:
                    if self.start % prime == 0:
                        break
                else:
                    self.prime_numbers.append(self.start)
                    return self.start


prime_number_iterator = PrimeNumbers(n=100)
for number in prime_number_iterator:
    print(number)
print('_' * 10)

# после подтверждения части 1 преподавателем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    end = n
    start = 1
    prime_numbers = []
    while start < end:
        start += 1
        for prime in prime_numbers:
            if start % prime == 0:
                break
        else:
            prime_numbers.append(start)
            yield start


for number in prime_numbers_generator(n=100):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном понимании - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
