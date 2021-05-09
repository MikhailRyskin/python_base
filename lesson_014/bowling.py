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
#  Кстати если ввести - 'ХXXXXXXXXX' с одной буквой "Х" кот валится с ошибкой
#  Сделайте замены символов для замены всех русских на анг или наоборот.
#  Для получения фреймов думаю удобнее сделать генератор "yield", который прокидывает по два символа из строки
def get_score(game_result):
    game_list = []
    print(' Количество очков для результатов', game_result, end=' : ')
    poz = 0
    for _ in range(10):
        if game_result[poz] == 'X':
            frame_result = 'X'
            poz += 1
        else:
            frame_result = game_result[poz] + game_result[poz + 1]
            poz += 2
        result = get_frame_score(frame_result)
        game_list.append(result)
        print(result, end=' ')
    return game_list


def get_frame_score(frame_result):
    try:
        check_frame_result(frame_result)
        if frame_result == 'X':
            result = 20
        elif frame_result[1] == '/':
            result = 15
        elif frame_result[0] == '-':
            if frame_result[1] == '-':
                result = 0
            else:
                result = int(frame_result[1])
        else:
            if frame_result[1] == '-':
                result = int(frame_result[0])
            else:
                result = int(frame_result[0]) + int(frame_result[1])
    except Exception as exp:
        result = 0
        print(exp, end=' ')
    finally:
        return result


def check_frame_result(res):
    first_poz = '123456789-'
    second_poz = '123456789/-'
    if len(res) < 1 or len(res) > 2:
        raise Exception(f'({res}:неверное количество позиций в результате)')
    if len(res) == 1:
        if res != 'X':
            raise Exception(f'({res}:если одна позиция - только strike)')
    else:
        if res[0] not in first_poz:
            raise Exception(f'({res}:1 позиция неверная)')
        if res[1] not in second_poz:
            raise Exception(f'({res}:2 позиция неверная)')
        if res.isdigit() and int(res[0]) + int(res[1]) > 9:
            raise Exception(f'({res}:сумма позиций больше 9)')
