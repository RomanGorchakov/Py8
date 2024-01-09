#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
from datetime import date


def get_plane():
    race = input("Название пункта назначения рейса: ")
    number = random.randint(1000, 9999)
    type = random.randint(1, 99)

    return {
        "race": race,
        "number": number,
        "type": type,
    }

def display_plane(staff):
    if staff:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 12
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
                "No",
                "Пункт назначения",
                "Номер рейса",
                "Тип самолёта"
            )
        )
        print(line)
 
        for idx, planes in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                    idx,
                    planes.get('race', ''),
                    planes.get('number', ''),
                    planes.get('type', 0)
                )
            )
 
    print(line)

def main():
    airport = []
    while True:
        command = input(">>> ").lower()
 
        if command == 'exit':
            break
 
        elif command == 'add':
            plane = get_plane()
 
            airport.append(plane)
            if len(airport) > 1:
                airport.sort(key=lambda item: item.get('race', ''))
 
        elif command == 'list':
            display_plane(airport)
 
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])
 
            count = 0
            for airports in airport:
                if airports.get('race') == sel:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, airports.get('race', ''))
                    )
                    print('Номер рейса:', airports.get('number', ''))
                    print('Тип самолёта:', airports.get('type', ''))
 
            if count == 0:
                print("Рейс не найден.")
 
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <товар> - информация о рейсе;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
 
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
            
if __name__ == '__main__':
    main()