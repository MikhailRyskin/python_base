from pony.orm import Database, Required, Json
from settings import DB_CONFIG


db = Database()
# db.bind(provider='postgres', user='', password='', host='', database='')
db.bind(**DB_CONFIG)

# class UserState:
#     """ Состояние пользователя внутри сценария."""
#     def __init__(self, scenario_name, step_name, context=None):
#         self.scenario_name = scenario_name
#         self.step_name = step_name
#         self.context = context or {}


class UserState(db.Entity):
    """ Состояние пользователя внутри сценария."""
    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)


class Registration(db.Entity):
    """ Сохранение регистраций."""
    name = Required(str)
    email = Required(str)


db.generate_mapping(create_tables=True)
