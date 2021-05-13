#  Создайте свои исключения, хотя бы пару
#  SpareError и StrikeError
#  .
#  Подсчет очков нужно доработать Примеры подсчета очков:
#  1) '81716151414333221154' - 63
#  2) 'XXXXXXXXXX' - 200
#  3) 'Х4/34-48/45173/X18' - 122
#  Подсчет очков на последнем примере.
#  Для удобства добавил нули, при страйке и  за место "-" нули, если кеглей не было сбито.
#  Можете по аналогии с моей разбивкой и добавлением символов реализовать это в функции.
#  Х  4/ 34 -4 8/ 45 17 3/ X  18
#  X0 4/ 34 04 8/ 45 17 3/ X0 18 - получаем такую строку после замены
#  .
#  X0 = 20 очков,
#  4/ = 15 очков, 35
#  34 = 7 очков, 42
#  04 = 4 очка, 46
#  8/ = 15 очков, 61
#  45 = 9 очков, 70
#  17 = 8 очков, 78
#  3/ = 15 очков, 93
#  Х0 = 20 очков, 113
#  18 = 9 очков.  122
#  Получается 122 очка. При спаре(8/, 3/)  цифра не важна, главное чтобы цифра не превышала количество кегль
#  .
#  В итоговом варианте возвращайте сумму, а не заставляйте пользователя браться за калькулятор

#  задание было сформулировано, мягко говоря, невнятно:
# "Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ."
# тут 3 икса и 3 игрека - полное впечатление, что нужно просто выводить количество очков для каждого фрейма
# Имеется ввиду что вводят "ХХХ" результатов бросков, а получаем "УУУ" количество очков.
#  Отлично доработали, но при неверном некорректном вводе лучше выбрасывать исключения с сообщениями, а не "None"
#  К примеру такие строки:
#   - 'rrrrrrrrrrrrrrrrrrrr' выбрасываем исключение ValueError
#   - '1X18/8/34X8/5/1854' выбрасываем исключение StrikeError
#   - 'Х4/94-48/45173/X18' выбрасываем исключение AttributeError к примеру.
#   Потому что вот здесь "94" результат броска превышающие кол-во кеглей
#   - 'XXXXX09XXXX' выбрасываем исключение ValueError. Потому что нуля не может быть в результате бросков

#  Кстати если ввести - 'ХXXXXXXXXX' с одной буквой "Х" кот валится с ошибкой
#  Сделайте замены символов для замены всех русских на анг или наоборот.
#  Для получения фреймов думаю удобнее сделать генератор "yield", который прокидывает по два символа из строки

class Not10FramesError(Exception):
    def __str__(self):
        return 'результат должен содержать 10 фреймов'


class SpareError(Exception):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f'символ spare на первой позиции в результате фрейма: {self.first}{self.second}'


class StrikeError(Exception):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f'символ strike на второй позиции в результате фрейма: {self.first}{self.second}'


def get_score(game_result, inter=False):
    game_result = game_result.replace('Х', 'X')
    mod_result = character_replacement(game_result)
    try:
        check_game_result(game_result)
        check_mod_result(mod_result)
        if inter:
            total_points = scoring_inter(mod_result)
        else:
            total_points = scoring(mod_result)
        print(f'Количество очков для результатов {game_result}: {total_points}')
        return total_points
    # Зачем здесь ловить ошибки? если они есть лучше их пробросить дальше т.к в любом случае программа завершится
    #  не очень понял, где ловить ошибки? В 01_score? А в турнире тогда где ловить?
    #  сейчас, как я понимаю, assertRaises в тестах не может работать, т.к. get_score не выбрасывает ошибки.
    # TODO Да все верно "assertRaises" не срабатывает потому что здесь вы эти ошибки обрабатываете.
    #  Здесь эти ошибки обрабатывать не нужно т.е нужно убрать из функции try\except
    except (Not10FramesError, ValueError, AttributeError, SpareError, StrikeError) as exp:
        print(exp)
        return str(exp)


def scoring(mod_result):
    total_points = 0
    poz = 0
    while poz < len(mod_result) - 1:
        first, second = mod_result[poz], mod_result[poz + 1]
        check_frame(first, second)
        if first == 'X':
            points = 20
        elif second == '/':
            points = 15
        else:
            points = int(first) + int(second)
        total_points += points
        poz += 2
    return total_points


def scoring_inter(mod_result):
    check_all_frames(mod_result)
    total_points = 0
    poz = 0
    not_last = True
    not_penult = True
    while poz < len(mod_result) - 1:
        first, second = mod_result[poz], mod_result[poz + 1]
        if first == 'X':
            points = strike_points_inter(mod_result, not_last, not_penult, poz)
        elif second == '/':
            points = spare_points_inter(mod_result, not_last, poz)
        else:
            points = int(first) + int(second)
        total_points += points
        poz += 2
        if poz == len(mod_result) - 4:
            not_penult = False
        if poz == len(mod_result) - 2:
            not_last = False
    return total_points


def spare_points_inter(mod_result, not_last, poz):
    points = 10
    if not_last:
        if mod_result[poz + 2] == 'X':
            points += 10
        else:
            points += int(mod_result[poz + 2])
    return points


def strike_points_inter(mod_result, not_last, not_penult, poz):
    points = 10
    if not_last:
        if mod_result[poz + 2] == 'X':
            points += 10
            if not_penult:
                if mod_result[poz + 4] == 'X':
                    points += 10
                else:
                    points += int(mod_result[poz + 4])
        else:
            if mod_result[poz + 3] == '/':
                points += 10
            else:
                points += int(mod_result[poz + 2]) + int(mod_result[poz + 3])
    return points


def character_replacement(result):
    modified_result = ''
    for symbol in result:
        if symbol == 'X':
            modified_result += 'X0'
        elif symbol == '-':
            modified_result += '0'
        else:
            modified_result += symbol
    return modified_result


def check_game_result(res):
    valid_characters = '123456789-/X'
    for char in res:
        if char not in valid_characters:
            raise ValueError(f'недопустимый символ в результате: {char}')
    was_already = 0
    check_line = list(res)
    number_of_x = check_line.count('X')
    for _ in range(number_of_x):
        strike_index = check_line.index('X')
        check_index = was_already + strike_index
        if check_index % 2 != 0:
            raise StrikeError(res[strike_index - 1], res[strike_index])
        was_already += 1
        check_line[strike_index] = 0


def check_mod_result(res):
    if len(res) != 20:
        raise Not10FramesError()


def check_frame(first_char, second_char):
    if first_char == '/':
        raise SpareError(first_char, second_char)
    elif first_char.isdigit() and second_char.isdigit():
        if int(first_char) + int(second_char) > 9:
            raise AttributeError(f'сумма позиций фрейма больше 9: {first_char}{second_char}')


def check_all_frames(mod_result):
    poz = 0
    while poz < len(mod_result) - 1:
        first, second = mod_result[poz], mod_result[poz + 1]
        check_frame(first, second)
        poz += 2
