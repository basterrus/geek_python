"""
Реализовать проект «Операции с комплексными числами». С
оздайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
 созданных экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNum:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return self.num_1 + self.num_2

    def __mul__(self, other):
        return self.num_1 * self.num_2


    def __str__(self):
        return f'Введенные числа {self.num_1} и {self.num_2};'\
               f' Сумма чисел {self.num_1} и {self.num_2} равна {self.num_1 + self.num_2};' \
               f' Произведение чисел {self.num_1} и {self.num_2} равно {self.num_1 * self.num_2}.' \


math = ComplexNum(10j, 20)
math_1 = ComplexNum(100, 200j)
print(math)
print(math_1)

# Не уверен что правильно понял ТЗ