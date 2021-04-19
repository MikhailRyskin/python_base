import os
import time


def file_path_generator(dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)
            yield full_file_path


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


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate
