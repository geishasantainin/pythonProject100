import DATABASE
import random

def contTinue(choice):


    # Вывести БД с пользователями
    if choice == '1':
        if len(DATABASE.users_list) > 0:
            for index, user in enumerate(DATABASE.users_list):

                max_len_stroke = int(len(user.login + user.password))

                if len(DATABASE.users_list) == 1:
                    print('┃    ┏' + '━' * (max_len_stroke + 5) + '┓' + ' ' * (156 - 13 - max_len_stroke)+'┃')
                    print('┃    ┃' + ' ' + str(user.login) + ' ', end='')
                    print('┃' + ' ' + str(user.password) + ' ' + '┃', end='')
                    print(' ' * (156 - 13 - max_len_stroke)+'┃')

                elif len(DATABASE.users_list) > 1:
                    print('┃    ┏' + '━' * (max_len_stroke + 5) + '┓' + ' ' * (156 - 13 - max_len_stroke)+'┃')
                    print('┃    ┃' + ' ' + str(user.login) + ' ', end='')
                    print('┃' + ' ' + str(user.password) + ' ' + '┃', end='')
                    print(' ' * (156 - 13 - max_len_stroke)+'┃')

            print('┃    ┗' + '━' * (max_len_stroke + 5) + '┛' + ' ' * (156 - 13 - max_len_stroke)+'┃')
            input("""┃                                                                                                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
        else:
            input('┃    ERROR: Database is empty.')


    # Вывести БД с фильмами
    elif choice == '2':
        if len(DATABASE.films_list) > 0:
            print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
            for index, film in enumerate(DATABASE.films_list):

                max_len_stroke = int(len(film.name + film.style + str(film.period)))

                if len(DATABASE.films_list) == 1:
                    print('┃    ┏' + '━' * (max_len_stroke + 8) + '┓' + ' '*(156-16-max_len_stroke)+'┃')
                    print('┃    ┃' + ' ' + str(film.name) + ' ', end='')
                    print('┃' + ' ' + str(film.style) + ' ', end='')
                    print('┃' + ' ' + str(film.period) + ' ' + '┃', end ='')
                    print(' '*(156-16-max_len_stroke)+'┃')

                elif len(DATABASE.films_list) > 1:
                    print('┃    ┏' + '━' * (max_len_stroke + 8) + '┓' + ' '*(156-16-max_len_stroke)+'┃')
                    print('┃    ┃' + ' ' + str(film.name) + ' ', end='')
                    print('┃' + ' ' + str(film.style) + ' ', end='')
                    print('┃' + ' ' + str(film.period) + ' ' + '┃', end='')
                    print(' ' * (156-16-max_len_stroke)+'┃')

            print('┃    ┗' + '━' * (max_len_stroke + 8) + '┛' + ' '*(156-16-max_len_stroke)+'┃')
            input("""┃                                                                                                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
        else:
            input('┃    ERROR: Database is empty.')


    # Вывести БД с залами
    elif choice == '3':
        if len(DATABASE.halls_list) > 0:
            print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
            for index, hall in enumerate(DATABASE.halls_list):

                max_len_stroke = int(len(hall.name + str(hall.num_of_rows) + str(hall.num_of_seats_in_row)))

                if len(DATABASE.halls_list) == 1:
                    print('┃    ┏'+'━' * (max_len_stroke + 8) + '┓' + ' ' * (156 - 16 - max_len_stroke) + '┃')
                    print('┃    ┃'+' ' + str(hall.name) + ' ', end='')
                    print('┃'+' ' + str(hall.num_of_rows) + ' ', end='')
                    print('┃'+' ' + str(hall.num_of_seats_in_row) + ' ' + '┃', end = '')
                    print(' ' * (156 - 16 - max_len_stroke) + '┃')

                if len(DATABASE.films_list) > 0:
                    print('┃    ┏'+ '━' * (max_len_stroke + 8) + '┓' + ' ' * (156 - 16 - max_len_stroke) + '┃')
                    print('┃    ┃' + ' ' + str(hall.name) + ' ', end='')
                    print('┃' + ' ' + str(hall.num_of_rows) + ' ', end='')
                    print('┃'+ ' ' + str(hall.num_of_seats_in_row) + ' ' + '┃', end = '')
                    print(' ' * (156 - 16 - max_len_stroke) + '┃')
            print('┃    ┗' + '━' * (max_len_stroke + 8) + '┛' + ' ' * (156 - 16 - max_len_stroke) + '┃')
            input("""┃                                                                                                                                                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
        else:
            input('┃    ERROR: Database is empty.')


    # Вывести Киноафишу
    elif choice == '4':
        print(
            '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')

        num_of_date = 0
        for i in range(3):
            day_object = DATABASE.Cinema_post(num_of_date, random.randint(1, 3))
            DATABASE.cinema_post_list.append(day_object)

        for object_day in DATABASE.cinema_post_list:
            print(f'{object_day.date}')
            for index, film in enumerate(object_day.films_in_date):
                print(f' {film.name} | {object_day.halls_in_date[index].name}')


    # Добавить фильм в БД
    elif choice == '5':
        print(
            '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')

        add_name_film = input('┃    Input film name: ')
        add_style_film = input('┃    Input film genre: ')
        add_period_film = input('┃    Input film duration:  ')

        film_object = DATABASE.Film(add_name_film, add_style_film, add_period_film)
        DATABASE.films_list.append(film_object)


    # Добавить кинозал в БД
    elif choice == '6':
        print(
            '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')

        add_name_hall = input('┃    Input hall name: ')
        add_num_of_rows_hall = input('┃    Input columns num: ')
        add_num_of_seats_in_row_hall = input('┃    Input rows num: ')

        hall_object = DATABASE.Hall(add_name_hall, add_num_of_rows_hall, add_num_of_seats_in_row_hall)
        DATABASE.halls_list.append(hall_object)


    # Удалить фильм из БД
    elif choice == '7':
        print(
            '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')

        if len(DATABASE.films_list) > 0:
            put = input('┃    Name of deleting film ')
            flag = False
            for object_film in DATABASE.films_list:
                if object_film.name == put:
                    flag = True
                    DATABASE.films_list.remove(object_film)
            if not (flag):
                input('┃    ERROR: Invalid input')


    # Удалить кинозал из БД
    elif choice == '8':
        print(
            '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')

        if len(DATABASE.halls_list) > 0:
            put = input('Name of deleting hall ')
            flag = False
            for object_hall in DATABASE.halls_list:
                if object_hall.name == put:
                    flag = True
                    DATABASE.halls_list.remove(object_hall)
            if not (flag):
                input('┃    ERROR: Invalid input')


    # Редактировать Киноафишу
    elif choice == '9':
        pass