#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from module2 import *


def main():
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
                add.add(lst)
            case 'phone':
                phone.phone(lst)
            case 'help':
                instructions.instruction()
            case 'list':
                list_workers.workers(lst)
            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == "__main__":
    main()
