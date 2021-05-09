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
