#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import sys
from module2 import add
from module2 import workers
from module2 import phone
from module2 import instruction


def main():
    sample = ['surname', 'name', 'phone', 'date']
    lst = []

    # ввод данных
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        match command:
            case 'exit':
                break
            case 'add':
                add(lst)
            case 'phone':
                phone(lst)
            case 'help':
                instruction()
            case 'list':
                workers(lst)
            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
