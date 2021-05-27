import re
from decimal import Decimal


class Dungeon:
    TOTAL_TIME = '123456.0987654321'
    HATCH_EXPERIENCE = 280

    def __init__(self, location_name, location):
        self.location_name = location_name
        self.location = location
        self.current_experience = 0
        self.current_time = 0
        self.remaining_time = Decimal(self.TOTAL_TIME)
        self.location_dict = {}
        self.location_monsters = []
        self.location_locations = []

        self.game_over = False
        self.revival = False

    def location_info(self):
        # выводим информацию о текущей локации, опыте и времени
        # формируем списки монстров и возможных локаций для перехода
        # формируем словарь текущей локации - название локации: индекс в списке локации
        print(f'\nВы находитесь в {self.location_name}')
        print(f'У вас {self.current_experience} опыта и осталось {self.remaining_time - self.current_time} '
              f'секунд до наводнения')
        print(f'Прошло времени: {self.current_time}\n')
        print('Внутри вы видите:')
        self.location_dict = {}
        self.location_monsters = []
        self.location_locations = []
        for elem_number, elem in enumerate(self.location):
            if isinstance(elem, str):
                elem_name = elem
                elem_line = f'Монстра {elem}'
                self.location_monsters.append(elem)
            else:
                for location in elem.keys():
                    elem_line = f'Вход в локацию: {location}'
                    self.location_locations.append(location)
                    elem_name = location
            print(elem_line)
            self.location_dict[elem_name] = elem_number
        print()

    def player_choice(self):
        print('Выберите действие:\n1.Атаковать монстра\n2.Перейти в другую локацию\n3.Сдаться и выйти из игры')
        choice = input('Ваш выбор: ')
        if choice == '1':
            self.choice_kill_monster()
        elif choice == '2':
            self.choice_change_location()
        else:
            print('Игра окончена')
            self.game_over = True

    def choice_kill_monster(self):
        if self.location_monsters:
            monster_name = self.location_monsters[0]
            if len(self.location_monsters) > 1:
                print('Выберите монстра для атаки:')
                for number, monster in enumerate(self.location_monsters):
                    print(f'{number + 1}.{monster}')
                monster_choice = int(input('Ваш выбор: '))
                monster_name = self.location_monsters[monster_choice - 1]
            self.kill_monster(monster_name)
        else:
            print('Нет монстров для атаки')

    def choice_change_location(self):
        if self.location_locations:
            self.location_name = self.location_locations[0]
            if len(self.location_locations) > 1:
                print('Выберите локацию для перехода:')
                for number, loc in enumerate(self.location_locations):
                    print(f'{number + 1}.{loc}')
                location_choice = int(input('Ваш выбор: '))
                self.location_name = self.location_locations[location_choice - 1]
            if self.location_name.startswith('Hatch'):
                if self.current_experience >= self.HATCH_EXPERIENCE:
                    print('You are winner!!!')
                    self.game_over = True
                else:
                    print('Вы нашли люк, но у Вас не хватает опыта! Это конец...')
                    self.resurrect()
            else:
                list_index = self.location_dict[self.location_name]
                temp_dict = self.location[list_index]
                self.location = temp_dict[self.location_name]
                self.add_time(self.location_name)
        else:
            print('Нет локаций для перехода')

    def kill_monster(self, monster_name):
        self.add_experience(monster_name)
        self.add_time(monster_name)
        self.location.remove(monster_name)

    def add_experience(self, element_name):
        re_exp = r'exp(\d+)'
        exp_str = re.search(re_exp, element_name)[1]
        self.current_experience += int(exp_str)

    def add_time(self, element_name):
        re_time = r'tm(\d+)'
        time_str = re.search(re_time, element_name)[1]
        self.current_time += Decimal(time_str)

    def resurrect(self):
        print('Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег!')
        self.revival = True

    def act(self):
        if self.location:
            self.location_info()
            if self.remaining_time - self.current_time < 0:
                print('Вы не успели найти люк!!! НАВОДНЕНИЕ!!!')
                self.resurrect()
            else:
                self.player_choice()
        else:
            print('Больше некуда идти! Тупик!!! Это конец...')
            self.resurrect()
