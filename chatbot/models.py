from pony.orm import Database, Required, Json
from ticket_settings import DB_CONFIG


db = Database()
# db.bind(provider='postgres', user='', password='', host='', database='')
db.bind(**DB_CONFIG)


class UserState(db.Entity):
    """ Состояние пользователя внутри сценария."""
    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)


class TicketInfo(db.Entity):
    """ Сохранение информации билета."""
    departure = Required(str)
    destination = Required(str)
    flight = Required(str)
    seats = Required(int)


db.generate_mapping(create_tables=True)
