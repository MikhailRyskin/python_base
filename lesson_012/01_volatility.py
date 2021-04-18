# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

#  написать код в однопоточном/однопроцессорном стиле
import os
import time

# TODO Предлагаю переработать логику и немного упростить класс.
#  То есть, классу передаем не всю папку "trades", а по одному "csv" файлу
#  Он обрабатывает информацию и возвращает данные по тикеру и волатильности.
#  .
#  С модулем "csv" это сделать проще почему вы его не использовали?
#  Классу достаточно будет двух методов.
#  1 - Получение информации
#  Создаем список цен и имя тикера
#  Создаем ридер "DictReader", и в цикле по ключам добавляем цены в список
#  Примерно так можно будет обращаться при создании "DictReader" - line['PRICE']
#  Собрали данные вернули - цены, имя тикера
#  2 - Расчет волатильности
#  Вызываем метод №1 и получаем все информацию
#  Делаем расчеты и возвращаем данные
#  .
#  Что касается того как передавать по одному пути в наш класс, здесь уже пригодится генератор.
#  Генератор сделать очень просто:
#  - цикл "os.walk"
#  - цикл по "filenames"
#  - склеиваем путь и возвращаем "yield"
#  .
#  Остается самое простое - это написать цикл который будет собирать словарь с волатильностью
class VolatilityCounter:

    tickers_volatility = dict()

    def __init__(self, data_dir_path, data_file):
        self.data_file = data_file
        self.data_dir_path = data_dir_path

    def volatility_calc(self, secid, price_list):
        half_sum = (max(price_list) + min(price_list)) / 2
        volatility = ((max(price_list) - min(price_list)) / half_sum) * 100
        self.tickers_volatility[secid] = round(volatility, 2)

    def run(self):
        full_file_path = os.path.join(self.data_dir_path, self.data_file)
        file = open(full_file_path, 'r')
        first_line = file.readline()
        price_list = []
        for line in file:
            secid, trade_time, price_str, quantity = line.split(',')
            price = float(price_str)
            price_list.append(price)
        file.close()
        self.volatility_calc(secid, price_list)


def output_result(result_dict):
    volatility_ticker = dict()
    for ticker, volatility in result_dict.items():
        if volatility in volatility_ticker:
            volatility_ticker[volatility].append(ticker)
        else:
            volatility_ticker[volatility] = [ticker]
    print('Максимальная волатильность:')
    for volatility in sorted(volatility_ticker.keys(), reverse=True)[:3]:
        for ticker in volatility_ticker[volatility]:
            print(f'    {ticker} - {volatility} %')
    print(' Минимальная волатильность:')
    min_volatility = sorted(volatility_ticker.keys(), reverse=True)
    if 0 in volatility_ticker:
        min_volatility = min_volatility[-4:-1]
    else:
        min_volatility = min_volatility[-3:-0]
    for volatility in min_volatility:
        for ticker in volatility_ticker[volatility]:
            print(f'    {ticker} - {volatility} %')
    print('Нулевая волатильность:')
    if 0 in volatility_ticker:
        print('   ', *volatility_ticker[0])


data_dir = 'trades'
started_at = time.time()

data_dir_path = os.path.abspath(data_dir)
for data_file in os.listdir(data_dir_path):
    vol_counter = VolatilityCounter(data_dir_path, data_file)
    vol_counter.run()

ended_at = time.time()
elapsed = round(ended_at - started_at, 2)
print(f'Функция работала {elapsed} секунд(ы)')

output_result(VolatilityCounter.tickers_volatility)
