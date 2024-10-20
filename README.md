# Ульяна Рогова курсовая работа "Проект 3. Поиск вакансий с подключением БД"

## Описание:

Разработка функционала для получения данных с сайта HH.ru, записью данных в БД PostgreSQL

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:AelitaDi/course_project_bd.git
```
2. Установите зависимости: mypy, flake8, black, isort, requests, psycopg2

## Применение:

1. Запустите модуль ``main.py``.
2. Введите ключевые слова для поиска компаний или оставьте выбор по умолчанию:
"HeadHunter", 
"ПАКС",
"Level Group",
"Роскосмос",
"институт теплотехники",
"сколково",
"Дело жизни",
"SkyPro",
"ГИБДД",
"DatsTeam". 
3. Введите название БД или оставьте название по умолчанию `headhunter`.
4. Программа создаст БД и две таблицы в ней `vacancies`, `companies`.
5. Программа выведет список компаний и количество открытых вакансий в каждой компании.
6. Далее вы можете выбрать расчетный случай:
1 - Вывести все вакансии ``get_all_vacancies``
2 - Вывести среднюю зарплату по вакансиям``get_avg_salary``
3 - Вывести вакансии с заработной платой выше среднего ``get_vacancies_with_higher_salary``
4 - Вывести вакансии по ключевому слову ``get_vacancies_with_keyword``
5 - Выход

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).