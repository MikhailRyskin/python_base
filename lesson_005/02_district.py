# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as room_01
from district.central_street.house1.room2 import folks as room_02
from district.central_street.house2.room1 import folks as room_03
from district.central_street.house2.room2 import folks as room_04
from district.soviet_street.house1.room1 import folks as room_05
from district.soviet_street.house1.room2 import folks as room_06
from district.soviet_street.house2.room1 import folks as room_07
from district.soviet_street.house2.room2 import folks as room_08
# Используйте простое сложение списков, тогда цикл вам будет не нужен .join все сделаем сам.
#  residents = (room_1 + room_2 ...
# TODO сделал сложение списков

# rooms_list = [room_01, room_02, room_03, room_04, room_05, room_06, room_07, room_08]
# total_folks = []
# for folks in rooms_list:
#     for folk in folks:
#         total_folks.append(folk)

total_folks =(room_01 + room_02 + room_03 + room_04 + room_05 + room_06 + room_07 + room_08)
print(', '.join(total_folks))
