# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stacionery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки...')


class Pen(Stacionery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки, выбран инструмент: {self.title}')

class Pencil(Stacionery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки, выбран инструмент: {self.title}')

class Handle(Stacionery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки, выбран инструмент: {self.title}')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

print(pen.draw())
print(pencil.draw())
print(handle.draw())
