"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    user_list = [
            {'name': 'Sergey', 'age': 48, 'job': 'Sailor'}, 
            {'name': 'Aleksandr', 'age': 34, 'job': 'Electrical engineer'}, 
            {'name': 'Aleksey', 'age': 27, 'job': 'Builder'},
            {'name': 'Dmitriy', 'age': 43, 'job': 'Oil Developer'},
        ]

    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        writer.writerows(user_list)

        
if __name__ == "__main__":
    main()
