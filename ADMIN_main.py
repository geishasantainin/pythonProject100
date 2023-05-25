import DATABASE
import ADMIN_menu_continue
import os
from DBase import Table
import pandas as pd



class Headline():
    def __init__(self):
        pass

    def create_headline(self, COLS:int, HEAD:str):
        self.COLS = COLS
        self.HEAD = HEAD
        SPACE_before = int( (COLS + 1 - len(HEAD)) / 2)
        SPACE_after = int(COLS + 1 - SPACE_before - len(HEAD))
        return (SPACE_before*'\033[44m\033[37m\033[1m ') + (HEAD) + (SPACE_after*' ') + ('\033[0m\n')

class Tab():
    def __init__(self):
        pass

    def create_tab(self, COLS:int, SPACE:int, TAB:tuple, num:int) -> str:
        self.COLS = COLS
        self.SPACE = SPACE
        self.TAB = TAB
        self.num = num
        st = str()
        LenTab = 0

        for i in TAB:
            LenTab += len(i)

        for ind, tab in enumerate(TAB):
            if ind == num:
                st += ('\033[30m\033[1m\033[47m') + (' ' * int(SPACE / 2)) + tab + (' ' * int(SPACE / 2))
            else:
                st += ('\033[37m\033[1m\033[44m') + (' ' * int(SPACE / 2)) + tab + (' ' * int(SPACE / 2))

        return ('\033[1m\033[37m\033[44m') + (' ' * int(SPACE / 2)) + ('\033[0m') + \
                (st) + ('\033[1m\033[37m\033[44m') + \
                 (' '*int(COLS + 1 - (int(SPACE / 2)+(LenTab)+(len(TAB)*SPACE)))) + ('\033[0m') + ('\n')

def outside(name, objects):
    table = pd.read_csv(os.path.abspath(f'{name}.csv'), sep=',')
    objects_list = []
    if name != 'users':
        for obj in objects:
            objects_list.append(obj.name)
        for t in list(table['name']):
            if t not in objects_list:
                table.drop(table[table['name'] == t].index, axis=0, inplace=True)
    else:
        for obj in objects:
            objects_list.append(obj.login)

        for t in list(table['log']):
            input((t, list(table['log'])))
            if t not in objects_list:
                table.drop(table[table['log'] == t].index, axis=0, inplace=True)
    table.to_csv(os.path.abspath(f'{name}.csv'), index=False)



def start_ADMIN_main():

    hd = Headline()
    tb = Tab()

    TABS = ('Users', 'Films', 'Halls', 'Movie Poster', 'Add Film', 'Add Hall', \
            'Remove Film', 'Remove Hall', 'Edit Movie_Poster', 'Exit')


    count = 0
    key = None
    while True:
        for index in range(len(TABS)):
            if index == count % len(TABS):
                os.system('CLS')
                print(hd.create_headline(155, 'ADMINISTRATOR SETUP MODE'), end='')
                print(tb.create_tab(155, 4, TABS, count%len(TABS)), end = '')
                print('\033[47m\033[34m' + '┏' + '━'*154 + '┓')
                print('┃' + ' '*154 +'┃')
                print('┃    ┏━━━━━━━━━━━━━━━━━━━━━━━┓'+125*' '+'┃')
                print('┃    ┃ Switch        [Enter] ┃'+125*' '+'┃')
                print('┃    ┃ Choose        [Space] ┃'+125*' '+'┃')
                print('┃    ┗━━━━━━━━━━━━━━━━━━━━━━━┛' + 125 * ' ' + '┃')
                key=input("""┃                                                                                                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")


        count += 1

        if key == ' ':
            if count % len(TABS) == 0:
                input('See you next time!')
                break
            else:
                ADMIN_menu_continue.contTinue(str((count) % len(TABS)))
                continue


        films_list = DATABASE.films_list
        halls_list = DATABASE.halls_list
        users_list = DATABASE.users_list

        for name in ['films', 'holls', 'users']:
            table = Table(name)
            if name == 'films':
                outside(name, films_list)
                for i, tb_obj in enumerate(films_list):
                    if not table.is_row_in_table([i, tb_obj.name, tb_obj.style, float(tb_obj.period), '-']):
                        table.append([i, tb_obj.name, tb_obj.style, float(tb_obj.period), '-'])

            elif name == 'holls':
                outside(name, halls_list)
                for i, tb_obj in enumerate(halls_list):
                    if not table.is_row_in_table(
                            [i, tb_obj.name, int(tb_obj.num_of_rows), int(tb_obj.num_of_seats_in_row)]):
                        table.append([i, tb_obj.name, int(tb_obj.num_of_rows), int(tb_obj.num_of_seats_in_row)])

            elif name == 'users':
                outside(name, users_list)
                for i, tb_obj in enumerate(users_list):
                    if not table.is_row_in_table([i, str(tb_obj.login), str(tb_obj.password)]):
                        table.append([i, str(tb_obj.login), str(tb_obj.password)])

