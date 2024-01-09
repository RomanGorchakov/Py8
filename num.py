#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date


def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def test():
    a = int(input("Введите число: "))
    if a > 0:
        return positive()
    else:
        return negative()

if __name__ == '__main__':
    test()