# TODO Создайте свои исключения, хотя бы пару
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

# TODO задание было сформулировано, мягко говоря, невнятно:
# "Скрипт должен принимать параметр --result и печатать на консоль:
#   Количество очков для результатов ХХХ - УУУ."
# тут 3 икса и 3 игрека - полное впечатление, что нужно просто выводить количество очков для каждого фрейма

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


def get_score(game_result):
    total_points = 0
    mod_result = character_replacement(game_result)
    try:
        check_game_result(mod_result)
        poz = 0
        while poz < len(mod_result) - 1:
            first, second = mod_result[poz], mod_result[poz + 1]
            check_frame_result(first, second)
            if first == 'X':
                points = 20
            elif second == '/':
                points = 15
            else:
                points = int(first) + int(second)
            total_points += points
            poz += 2
        print(f'Количество очков для результатов {game_result}: {total_points}')
        return total_points
    except (Not10FramesError, ValueError, SpareError) as exp:
        print(exp)


def character_replacement(result):
    modified_result = ''
    for symbol in result:
        if symbol == 'X' or symbol == 'Х':
            modified_result += 'X0'
        elif symbol == '-':
            modified_result += '0'
        else:
            modified_result += symbol
    return modified_result


def check_game_result(res):
    valid_characters = '0123456789/X'
    if len(res) != 20:
        raise Not10FramesError()
    for char in res:
        if char not in valid_characters:
            raise ValueError(f'недопустимый символ в результате: {char}')


def check_frame_result(first_char, second_char):
    if first_char == '/':
        raise SpareError(first_char, second_char)
    elif first_char.isdigit() and second_char.isdigit():
        if int(first_char) + int(second_char) > 9:
            raise ValueError(f'сумма позиций фрейма больше 9: {first_char}{second_char}')
