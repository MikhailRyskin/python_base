# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью функций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
import my_burger


def double_cheeseburger():
    print('Рецепт двойного чизбургера:')
    my_burger.bun()
    my_burger.cutlet()
    my_burger.cheese()
    my_burger.cucumber()
    my_burger.cutlet()
    my_burger.cheese()
    my_burger.cucumber()
    my_burger.mayo()


def my_choice_burger():
    print('Рецепт моего бургера:')
    my_burger.bun()
    my_burger.cucumber()
    my_burger.cutlet()
    my_burger.tomato()
    my_burger.mayo()


double_cheeseburger()
print()
my_choice_burger()

# зачет!
