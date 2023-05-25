from DBase import Table
import USER_utilits

class Film:
    def __str__(self):
        print(self.name)
    def __init__(self, name:str, style:str, period:int):
        self.name = name
        self.style = style
        self.period = period


class User:
    def __str__(self):
        print(self.login, self.password)
    def __init__(self, login:str, password:str):
        self.login = login
        self.password = password


class Hall:
    def __str__(self):
        print(self.name)
    def __init__(self, name:str, num_of_rows:int, num_of_seats_in_row:int):
        self.name = name
        self.num_of_rows = num_of_rows
        self.num_of_seats_in_row = num_of_seats_in_row


films_list = list()
users_list = list()
halls_list = list()

h1 = Hall('Star', 3, 3)
h2 = Hall('Wars', 4, 4)
h3 = Hall('Falcon', 5, 5)



dates = ['26.05', '27.05', '28.05']

films = []
for obj_flm in films_list:
    films.append(obj_flm.name)

film_tiles = [USER_utilits.Tile(flm) for flm in films]
date_tiles = [USER_utilits.Tile(date) for date in dates]


for tb in ['films', 'holls', 'users']:
    table = Table(tb).get_collection_by_index()
    for row in table:
        if tb == 'films':
            films_list.append(Film(str(row[1]), str(row[2]), str(row[3])))
        elif tb == 'holls':
            halls_list.append(Hall(str(row[1]), str(row[2]), str(row[3])))
        elif tb == 'users':
            users_list.append(User(str(row[1]), str(row[2])))


the_first_day = {'Imperia Strikes Back':halls_list[2],
                'Mandalorian':halls_list[1],
                'Fallen Jedi':halls_list[2],
                'Star Wars Part1':halls_list[0],
                'Star Wars Part2':halls_list[0]}

the_second_day = {'Avengers':halls_list[1],
                'Harry Potter: Philosophy Stone':halls_list[2],
                'Harry Potter: Chamber of Secrets':halls_list[1],
                'Harry Potter: Goblet of Fire':halls_list[0],
                'Harry Potter: Deathly Hallows':halls_list[2]}

the_third_day = {'Astral':halls_list[0],
                'Friday the 13th':halls_list[2],
                'Wrong Turn':halls_list[0],
                'It':halls_list[1],
                'The Conjuring':halls_list[1]}
