#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_input():
    return input()

def test_input(x):
    if (type(x) == int) or (type(x) == float):
        return True

    elif x.isnumeric():
        return True

    else:
        return False

def str_to_int(x):
    return int(x)

def print_int(x):
    print(x)


if __name__ == '__main__':
    x = get_input()
    if test_input(x):
        print_int(str_to_int(x))