"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_today = date.today()
    print(dt_today)

    delta = timedelta(days = 1)
    dt_yerstaday = dt_today - delta
    print(dt_yerstaday)

    delta = timedelta(days = 30)
    dt_30_days_ago = dt_today - delta
    print(dt_30_days_ago)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = "01/01/20 12:10:03.234567"
    str_2_datetime = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    print(str_2_datetime)


if __name__ == "__main__":
    print_days()

