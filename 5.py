# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# Запрашиваем у пользователя входные параметры
proceed = int(input('Введите значение выручки Вашей фирмы: '))  # Выручка
costs = int(input('Введите значение издержек Вашей фирмы: '))   # Издержки
personal = int(input('Введите количество сотрудников Вашей фирмы: '))   # Количество людей


# Определение финансового результата
profit = proceed - costs  # Прибыль
profitability = profit / proceed  # Рентабельность
profit_per_employee = profit / personal     # Прибыль/Убыток в рассчете на одного сотрудника
if profit > 0:
    print(f'    Поздравляем! Ваша фирма приносит прибыль \n'
          f'    Рентабельность Вашего предприятия равна: {profitability} \n'
          f'    Прибыль на одного сотрудника Вашей фирмы равна: {profit_per_employee:.2f} денежных единиц')
else:
    print(f'    Сожалеем, Ваша фирма приносит убыток \n'
          f'    Рентабельность Вашего предприятия равна: {profitability} \n'
          f'    Убыток с одного сотрудника Вашей фирмы равен:  {profit_per_employee:.2f} денежных единиц')
