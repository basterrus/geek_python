# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

# script_name, production, cost_in_hour, prize = argv

production = int(argv[1])
cost_in_hour = int(argv[2])
prize = int(argv[3])


def wage():
    result = production * cost_in_hour + prize
    print(f'Вам начислена зарплата: - {result}')


wage()
