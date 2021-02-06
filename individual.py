# Даны стороны прямоугольника. Найти его периметр и длину диагонали.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == "__main__":
    width = input("The width of the rectange:")
    length = input("The length of the rectangle")
    width = int(width)
    length = int(length)

    perimeter = width*2 + length*2
    diagonal = math.sqrt(width*width + length*length)
    perimeter = str(perimeter)
    diagonal = str(diagonal)

    print("The perimeter is equal to " + perimeter)
    print("The diagonal is " + diagonal)