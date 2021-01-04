"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    def get_square_coat(self):
        return self.size / 6.5 + 0.5

    def get_square_suit(self):
        return self.growth * 2 + 0.3

    @property
    def full_squer_material(self):
        return str((self.size / 6.5 + 0.5) + (self.growth * 2 + 0.3))


class Coat(Clothes):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.get_square_coat = self.size / 6.5 + 0.5

    def __str__(self):
        return f'{self.get_square_coat}'


class Suit(Clothes):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.get_square_suit = self.growth * 2 + 0.3

    def __str__(self):
        return f'{self.get_square_suit}'


coat = Coat(2, 3)
suit = Suit(1.5, 5)
print(f'Общая потребность материала на пальто: {coat.full_squer_material:.4}')
print(f'Общая потребность материала на пальто: {suit.full_squer_material:.4}')
print(f'Требуется всего материала на пальто: {coat.get_square_coat:.2}')
print(f'Требуется всего материала на костюм: {suit.get_square_suit}')
