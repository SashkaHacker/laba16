#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


def add(lst):
    surname = input('Фамилия: ')
    name = input("Имя: ")
    phone = input("Номер телефона: ")
    date = input('Дата рождения (число:месяц:год): ').split(':')

    # Создать словарь.
    dct = {'surname': surname,
           'name': name,
           'phone': phone,
           'date': date}
    lst.append(dct)

    # Сортировка списка словарей
    lst.sort(key=lambda x:
    datetime.strptime('-'.join(x['date']), '%d-%m-%Y'))

