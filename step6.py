# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# (1, {'Наименование': 'Смартфон Apple', 'Цена': '50000', 'Количество': '2', 'ЕИ': 'штука'})

product_db = []
count = 0
name = input('Введите наименование товара: ')
price = int(input('Введите цену товара: '))
quantity = int(input('Введите количество товара: '))

product_db.extend(count, {name})
print(product_db)


# for k, v in data.items():
#     print(k, ":", v)

