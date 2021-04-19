# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
# Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# тут ваш код в многопоточном стиле
import os
import threading
import csv
from utils import file_path_generator, output_result, time_track


class VolatilityCounter(threading.Thread):

    def __init__(self, data_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_file = data_file
        self.ticker = ''
        self.volatility = 0

    def run(self):
        ticker, price_list = self.get_data()
        half_sum = (max(price_list) + min(price_list)) / 2
        volatility = ((max(price_list) - min(price_list)) / half_sum) * 100
        self.ticker = ticker
        self.volatility = round(volatility, 2)

    def get_data(self):
        price_list = []
        with open(self.data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ticker = row['SECID']
                price_list.append(float(row['PRICE']))
        return ticker, price_list


@time_track
def main():
    data_dir = 'trades'
    tickers_volatility = dict()
    data_dir_path = os.path.abspath(data_dir)
    # TODO Добавьте в конструктор тикеров, чтобы здесь сразу их передавать в словарь.
    #  То есть чтобы создавать класс таким образом VolatilityCounter(data_file=data_file, tikers=tickers_volatility)
    vol_counters = [VolatilityCounter(data_file) for data_file in file_path_generator(data_dir_path)]
    for vol_counter in vol_counters:
        vol_counter.start()
    for vol_counter in vol_counters:
        vol_counter.join()
    # TODO Тогда это не понадобится, потому что после "join" словарь будет наполнен данными
    for vol_counter in vol_counters:
        tickers_volatility[vol_counter.ticker] = vol_counter.volatility
    output_result(tickers_volatility)


if __name__ == '__main__':
    main()
