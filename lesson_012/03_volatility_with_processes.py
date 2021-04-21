# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
# Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

# тут ваш код в многопроцессном стиле
import os
import multiprocessing
import csv
from utils import file_path_generator, output_result, time_track


class VolatilityCounter(multiprocessing.Process):

    def __init__(self, data_file, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_file = data_file
        self.collector = collector

    def run(self):
        ticker, price_list = self.get_data()
        half_sum = (max(price_list) + min(price_list)) / 2
        volatility = ((max(price_list) - min(price_list)) / half_sum) * 100
        volatility = round(volatility, 2)
        self.collector.put((ticker, volatility))

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
    collector = multiprocessing.Queue()
    tickers_volatility = dict()
    data_dir_path = os.path.abspath(data_dir)

    vol_counters = [VolatilityCounter(data_file, collector)
                    for data_file in file_path_generator(data_dir_path)]
    for vol_counter in vol_counters:
        vol_counter.start()
    for vol_counter in vol_counters:
        vol_counter.join()
    while not collector.empty():
        ticker, volatility = collector.get()
        tickers_volatility[ticker] = volatility
    output_result(tickers_volatility)


if __name__ == '__main__':
    main()

# зачет!
