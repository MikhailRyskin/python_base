# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database

from weather_engine import WeatherMaker, DatabaseUpdater, ImageMaker, handle_date
# TODO Весь основной код сделайте функцией, и вызывайте ее в конструкции if __name__ == '__main__'
forecast = WeatherMaker()
forecast.weather_parser()
# TODO Класс с базой вроде есть, метод добавления есть, погода парсится.
#  А погоду в базу почему сразу не добавляете?
forecast_base = DatabaseUpdater(forecast.forecast_dict)

not_exit = True
while not_exit:
    # TODO Если строки длинные делайте переносы, и лучше сразу записывать нужные строки в "input"
    #  а не использовать дополнительный print
    print('\nВыберите действие: 1. добавить прогноз в базу данных. 2. Получить прогноз из базы данных. '
          'Иначе - завершение программы:', end=' ')
    choice = input()
    if choice == '1':
        print('Занесение прогноза в базу данных.')
        input_date, time_range = handle_date()
        date_dt, date_rus = forecast.date_conversion(input_date)
        if forecast_base.save_forecast(date_dt, time_range):
            print(f'прогноз с {date_rus} на {time_range} дней занесён в базу данных')
        else:
            print('Нет прогноза на этот период')
    elif choice == '2':
        print('Получение прогноза из базы данных.')
        input_date, time_range = handle_date()
        date_dt, date_rus = forecast.date_conversion(input_date)
        forecast_list = forecast_base.get_forecst(date_dt, time_range)
        if forecast_list:
            print('Выберите действие: 1. создать открытку из прогноза. 2. Вывести прогноз на консоль.:', end=' ')
            output_choice = input()
            if output_choice == '1':
                for number, day_forecast in enumerate(forecast_list):
                    # TODO Экземпляры классов лучше создавать вне циклов и условий
                    im = ImageMaker(day_forecast.date_rus, day_forecast.temperature, day_forecast.weather)
                    im.generate_image(number)
                print('открытки сохранены в файлах weather_img_х.jpg')
            elif output_choice == '2':
                for day_forecast in forecast_list:
                    print(f'Прогноз на {day_forecast.date_rus}: {day_forecast.temperature},  {day_forecast.weather}.')
            else:
                print('Неверный выбор.')
        else:
            print('Прогноза на этот период нет в базе')
    else:
        not_exit = False
        print('Конец работы.')
