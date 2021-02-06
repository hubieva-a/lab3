# Запросите у пользователя четыре числа (файл numbers.py). Отдельно сложите первые два и
# отдельно вторые два. Разделите первую сумму на вторую. Выведите результат на экран так,
# чтобы ответ содержал две цифры после запятой.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    firstnumber = input("Please enter a number ")
    secondnumber = input("Please enter another number ")
    thirdnumber = input("Please enter another number ")
    fourthnumber = input("Please enter another number ")

    firstnumber = int(firstnumber)
    secondnumber =int(secondnumber)
    thirdnumber = int(thirdnumber)
    fourthnumber = int(fourthnumber)

    firstsecondsum = firstnumber + secondnumber
    thirdfourthsum = thirdnumber + fourthnumber
    division = firstsecondsum/thirdfourthsum
    print(round(division, 2))
