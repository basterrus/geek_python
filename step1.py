"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, date_month_year):
        self.date_month_year = str(date_month_year)

    @classmethod
    def transformation(cls, date_month_year):
        data = []
        for i in date_month_year.split():
            if i != '-':
                data.append(i)

        return int(data[0]), int(data[1]), int(data[2])

    @staticmethod
    def valid( day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return day, month, year
                else:
                    return f'Вы ввели не правильный год!'
            else:
                return f'Вы ввели не правильный месяц!'
        else:
            return f'Вы ввели не правильную дату!!'


    def __str__(self):
        return f'Текущая дата {Data.transformation(self.date_month_year)}'


today = Data('18 - 01 - 2021')
print(today)
print(Data.valid(11, 11, 2025))
print(Data.valid(11, 13, 2021))
print(Data.valid(34, 11, 2021))
print(today.valid(34, 13, 2028))
print(Data.transformation('18 - 01 - 2021'))
print(today.transformation('18 - 01 - 2021'))

