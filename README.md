﻿
## `                                                          `**ПРОЕКТ**
IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. Этот проект, который на бэкенде будет готовить данные для отображения в новом виджете.

ЗАДАНИЕ ПЕРВОЕ

1\. Организуйте ваш проект — создайте основные пакеты: 

src

` `— для исходного кода, 

tests

` `— для          тестов.

2\. Установите инструменты для проверки качества кода (Flake8, 

black

, 

isort

, 

mypy

) в группу 

`  `lint

` `через Poetry.

3\. Настройте файл 

.flake8

` `для конфигурации линтера Flake8.

4\. Добавьте конфигурации для 

black

, 

isort

` `и 

mypy

` `в файл 

pyproject.toml

.

5\. В пакете 

src

` `создайте модуль с названием 

masks

.

6\. Реализуйте в этом модуле две функции:

Функцию маскировки номера банковской карты 

get\_mask\_card\_number

.

Функцию маскировки номера банковского счета 

get\_mask\_account

.

7\. Запустите линтер Flake8 для проверки стиля кода.

8\. Используйте 

black

` `и 

isort

` `для форматирования кода.

10\. Проведите статический анализ типов с помощью 

mypy

, чтобы убедиться в отсутствии ошибок типизации в коде.

Как работают функции

Функция 

get\_mask\_card\_number

` `принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате 

XXXX XX\*\* \*\*\*\* XXXX

, где 

X

` `— это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:

7000792289606361     # входной аргумент

7000 79\*\* \*\*\*\* 6361  # выход функции

Функция 

get\_mask\_account

` `принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате 

\*\*XXXX

, где 

X

` `— это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки. Пример работы функции:

73654108430135874305  # входной аргумент

\*\*4305  # выход функции







