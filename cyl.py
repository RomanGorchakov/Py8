#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


def circle(r):
    return math.pi * (r ** 2)

def cylinder(r, h):
    q = input("Что вы хотите получить: площадь боковой поверхности цилиндра или полную площадь цилиндра? ")

    if q == "Площадь боковой поверхности":
        return 2 * math.pi * r * h
    elif q == "Полную площадь":
        return 2 * math.pi * r * h * circle(r)

if __name__ == '__main__':
    r = int(input("Радиус окружности: "))
    h = int(input("Высота цилиндра: "))
    print(cylinder(r, h))