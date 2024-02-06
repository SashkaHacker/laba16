#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def workers(lst):
    if lst:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15,
            '-' * 15
        )
        print(line)
        print(f'| {"№":^4} | {"Фамилия":^30} | {"Имя":^20} | '
              f'{"Номер телефона":^15} | {"Дата рождения":^15} |')

        print(line)
        for idx, worker in enumerate(lst, 1):
            print(f"")
            print(f'| {idx:>4} | {worker.get("surname", ""):<30} | '
                  f'{worker.get("name", ""):<20}'
                  f' | {worker.get("phone", 0):>15}'
                  f' | {":".join(worker.get("date", 0)):>15} |')

        print(line)
    else:
        print("Список работников пуст.")
