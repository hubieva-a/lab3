# Напишите программу (файл user.py), которая запрашивала бы у пользователя:
# его имя (например, "What is your name?")
# возраст ("How old are you?")
# место жительства ("Where are you live?")
# После этого выводила бы три строки:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    whatsyourname = input("What is your name?")
    howoldareyou = input("How old are you?")
    wheredoyoulive = input("Where do you live?")

    print("This is " + whatsyourname)
    print("(S)he is " + howoldareyou)
    print("(S)he lives in " + wheredoyoulive)


