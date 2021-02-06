# Напишитепрограмму(файл arithmetic.py), которая предлагала бы пользователю решить пример
# 4 * 100 - 54. Потом выводила бы на экран правильный ответ
# и ответ пользователя. Подумайте, нужно ли здесь преобразовывать строку в число.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    usersanswer = input("Please solve this: 4 * 100 - 54 = ")
    correctanswer = 346
    correctanswer = str(correctanswer)

    print("Your answer: " + usersanswer)
    print("Correct answer: " + correctanswer)