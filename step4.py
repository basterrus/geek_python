# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#


numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',

}

new_numbers = []


def openfile():
    with open('step4.dat', 'r') as file1:
        for i in file1:
            i = i.split(' ', 1)
            new_numbers.append(numbers[i[0]] + '  ' + i[1])
        print(new_numbers)


def writefile():
    with open('file4new.dat', 'w') as file2:
        file2.writelines(new_numbers)


openfile()
writefile()