#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
#  здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
#  здесь ваш код
all_flowers = garden_set | meadow_set
print(*all_flowers)

# выведите на консоль те, которые растут и там и там
# здесь ваш код
common_flowers = garden_set & meadow_set
print(*common_flowers)
# выведите на консоль те, которые растут в саду, но не растут на лугу
#  здесь ваш код
garden_notmeadow = garden_set - meadow_set
print(*garden_notmeadow)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# здесь ваш код
meadow_notgarden = meadow_set - garden_set
print(*meadow_notgarden)

# зачет!
