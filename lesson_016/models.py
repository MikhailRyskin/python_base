import peewee

database = peewee.SqliteDatabase('weather_forecast.db')


class BaseTable(peewee.Model):
    class Meta:
        database = database


class WeatherBase(BaseTable):
    date = peewee.DateTimeField()
    date_rus = peewee.CharField()
    temperature = peewee.CharField()
    weather = peewee.CharField()


database.create_tables([WeatherBase, ])
