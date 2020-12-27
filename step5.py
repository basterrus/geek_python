# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def write_numbers():
    with open('step5.dat', 'w', encoding='UTF-8') as f:
        num = input('Введите через пробел несколько чисел, после нажмите ВВОД: ')
        f.write(num)


def read_file_summ():
    with open('step5.dat', 'r', encoding='UTF-8') as f:
        new_num = f.read()
        print(f'Сумма введенных чисел равна: {sum([int(num) for num in new_num.split()])}')


write_numbers()
read_file_summ()