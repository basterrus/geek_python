# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

def openfile():
    pass


def average():
    pass

basefile = {}

with open('step3.dat', 'r', encoding='utf-8') as f:
    base = f.readline().split(' ')

    print(base)
    print(type(base))
    print(type(basefile))