"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDevision:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def zero_devision(number_1, number_2):
        try:
            return number_1 / number_2
        except:
            return f'На ноль делить ЗАПРЕЩЕНО!'


zero = ZeroDevision(25, 5)
print(ZeroDevision.zero_devision(25, 0))
print(ZeroDevision.zero_devision(25, 0.5))
print(zero.zero_devision(50, 0))