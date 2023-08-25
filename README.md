## Домашнее задание к лекции 1. «Import. Module. Package»

Основной код находится в файле [main.py](https://github.com/NadezhdaLimanova/accounting/blob/master/main.py)

Зависимости находятся в файле [requirements.txt](https://github.com/NadezhdaLimanova/accounting/blob/master/requirements.txt)

Необязательное задание [dirty_main](https://github.com/NadezhdaLimanova/accounting/blob/master/dirty_main.py)

## Задание 

Разработать структуру программы «Бухгалтерия»:

1. main.py;
2. application/salary.py;
3. application/db/people.py.
   
Main.py — основной модуль для запуска программы.

В модуле salary.py функция calculate_salary.

В модуле people.py функция get_employees.

Импортировать функции в модуль main.py и вызывать эти функции в конструкции.

if __name__ == '__main__':

Сами функции реализовывать не нужно. Достаточно добавить туда какой-либо вывод.

Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.

Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией. При желании можно написать программу с этим пакетом.

## Необязательное задание. 

Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции.

from package.module import *
