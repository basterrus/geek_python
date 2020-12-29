# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}



class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)


    def get_full_name(self):
        return f'ФИО: {self.name} {self.surname}\nДолжность: {self.position}'

    def get_total_income(self):
        total = int(self._income.get('wage')) + int(self._income.get('bonus'))
        return f'Зарплата с учетом премии: {total}₽'

position = Position('Иван','Иванов', 'Генеральный директор ООО\"РОМАШКА\"', 50000, 500)
position1 = Position('Петр','Петров', 'Главный инженер ООО\"РОМАШКА\"', 40000, 400)
position2 = Position('Василий','Тазиков', 'Директор по качеству ООО\"РОМАШКА\"', 30000, 300)
print(position.get_full_name())
print(position.get_total_income())
print('*'*50)
print(position1.get_full_name())
print(position1.get_total_income())
print('*'*50)
print(position2.get_full_name())
print(position2.get_total_income())
