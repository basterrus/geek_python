# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.


def lenth_lines_func():
    with open('step2.txt', 'r', encoding='utf-8') as f:
        print(f'Количество строк в файле равное: {len(f.readlines())}')


def quantity_words_in_line():
    with open('step2.txt', 'r', encoding='utf-8') as f:
        temp = f.readlines()
        for i in range(len(temp)):
            print(f'Колличество символов в {i + 1}ой строке равно {len(temp[i])}')  # Не пойму почему в первой строке
                                                                                    # 6, а не 5 символов


lenth_lines_func()
quantity_words_in_line()
