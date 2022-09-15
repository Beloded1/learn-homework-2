"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as fs:
        return fs.read()



def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    content = read_file('referat.txt') 

    print(f"Длина получившейся строки: {len(content)}")
        
    first_result = len(content.split())
    print(f"Количество слов в тексте: {first_result}")

    changed_content = content.replace('.', '!')
    write_file("referat_output2.txt", changed_content)

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as my_ref_3:
        my_ref_3.write(content)
            


if __name__ == "__main__":
    main()
