#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def phone(lst):
    numbers_phone = input('Введите номер телефона')
    fl = True
    for i in lst:
        if i['phone'] == numbers_phone:
            print(f"Фамилия: {i['surname']}\n"
                  f"Имя: {i['name']}\n"
                  f"Номер телефона: {i['phone']}\n"
                  f"Дата рождения: {':'.join(i['date'])}")
            fl = False
            break
    if fl:
        print("Человека с таким номером телефона нет в списке.")