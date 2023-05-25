import os

import DBase
import USER_utilits
import DATABASE


class User:
    def __init__(self):
        self.choose_date = 0
        self.choose_movie = 0

    def choosing_date(self):
        count = 0
        while True:  # вывод на консоль даты
            USER_utilits.print_tile(DATABASE.date_tiles, count)
            key = input()

            if key == ' ':
                choose_date = count % len(DATABASE.date_tiles)
                os.system('CLS')
                return (choose_date)
            count += 1

    def choose_film(self, choose_date: int):
        flms_f_28 = [USER_utilits.Tile(i) for i in DATABASE.films_for_28]
        flms_f_29 = [USER_utilits.Tile(i) for i in DATABASE.films_for_29]
        flms_f_30 = [USER_utilits.Tile(i) for i in DATABASE.films_for_30]

        count = 0
        if choose_date == 0:  # 28.04, фильмы
            while True:
                USER_utilits.print_tile(flms_f_28, count)
                key = input()

                if key == ' ':
                    choose_movie = count % len(flms_f_28)
                    os.system('CLS')
                    return (flms_f_28[choose_movie].text)
                count += 1


        elif choose_date == 1:  # 29.04, фильмы
            while True:
                USER_utilits.print_tile(flms_f_29, count)
                key = input()

                if key == ' ':
                    choose_movie = count % len(flms_f_29)
                    os.system('CLS')
                    return (flms_f_29[choose_movie].text)
                count += 1


        elif choose_date == 2:  # 30.04, фильмы
            while True:
                USER_utilits.print_tile(flms_f_30, count)
                key = input()

                if key == ' ':
                    choose_movie = count % len(flms_f_30)
                    os.system('CLS')
                    return (flms_f_30[choose_movie].text)
                count += 1

    def choosing_seat(self, choose_date: int, choose_movie: int):
        spi = [DATABASE.films_for_28, DATABASE.films_for_29, DATABASE.films_for_30]
        tbl = DBase.Table('sessions')

        num = None

        for y in range(15):
            if str(tbl.get_element(id=y, coulumn=4)) == DATABASE.dates[choose_date] and \
                    tbl.get_element(id=y, coulumn=3) == (spi[choose_date][choose_movie]).name and \
                    tbl.get_element(id=y, coulumn=2) == choose_movie:

                res = str(tbl.get_element(id=y, coulumn=5)[1:-1])

                list_seats = [str(x) for x in res]
                seats = []
                for i in list_seats:
                    if i == '0':
                        seats.append('[]')
                    else:
                        seats.append('//')

                count = 0

                if (spi[choose_date][choose_movie]).name == 'Falcon':
                    count = 5
                elif (spi[choose_date][choose_movie]).name == 'Wars':
                    count = 4
                else:
                    count = 3

                list_tiles = [USER_utilits.Tile(element) for element in seats]

                result, num = USER_utilits.columns_tile(list_tiles, int(count))

                print(result)

                res_seats = '(' + res[:num] + '1' + res[num + 1:] + ')'
                tbl.set_element(id=y, coulumn=5, data=res_seats)


def start_USER_main():
    user1 = User()
    ch_date = user1.choosing_date()
    ch_movie = user1.choose_film(ch_date)
    user1.choosing_seat(ch_date, ch_movie)
