import DATABASE
import DBase

from ADMIN_main import start_ADMIN_main
from USER_main import start_USER_main

while True:
    l = input("Enter your login: ")
    p = input("Enter your password: ")

    ERROR_log = [' ' * x for x in range(0, 21)]

    if l == 'admin' and p == 'admin':
        start_ADMIN_main()

    elif ((l in ERROR_log) or (l[0].isalpha() == False) or (len(l) < 5) or (len(l) > 20)) and \
            ((p == l) or (p in ERROR_log) or (len(p) < 6) or (len(p) > 30)):
        print('\033[0m\033[31m[ERROR]: Invalid input')
        input(
            '\033[0m\033[5m[RULE]: Password must be from 6 to 30 symbols and not similar with the login')

    elif (l in ERROR_log) or (l[0].isalpha() == False) or (len(l) < 4) or (len(l) > 20):
        print('\033[0m\033[31m[ERROR]: Invalid input')
        input(
            '\033[0m\033[5m[RULE]: Login must be from 4 to 30 symbols and it must starts with the letter')

    elif (p == l) or (p in ERROR_log) or (len(p) < 6) or (len(p) > 30):
        print('\033[0m\033[31m[ERROR]: Invalid input')
        input(
            '\033[0m\033[5m[RULE]: Password must be from 6 to 30 symbols and not similar with the login')

    else:
        user_object = DATABASE.User(l, p)
        DATABASE.users_list.append(user_object)
        start_USER_main()

