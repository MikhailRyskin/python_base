# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# import room_1
from room_1 import folks as folks_room_1
# from room_1 import folks

# import room_2
# from .room_2 import folks
# TODO не понимаю, почему не работает from .room_2 import folks
#  вроде 01_inhabitants.py находится в пакете lesson_005  на одном уровне с room_2.py

from lesson_005.room_2 import folks

# print('В комнате room_1 живут:', *room_1.folks)
print('В комнате room_1 живут:', *folks_room_1)
# print('В комнате room_1 живут:', *folks)

# print('В комнате room_2 живут:', *room_2.folks)
print('В комнате room_2 живут:', *folks)

# зачет!
