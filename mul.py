#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


def multiply():
    x = int(input("Введите число: "))

    if x == 0:
        exit()
    
    mult = 1
    
    while x != 0:
        mult *= x
        print(mult)
        x = int(input("Введите число: "))


if __name__ == '__main__':
    multiply()