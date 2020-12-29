# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def Go(self):
        return f'{self.name} поехал'

    def Stop(self):
        return f'{self.name} остановился'

    def Turn_Left(self):
        return f'{self.name} повернул налево'

    def Turn_Rigth(self):
        return f'{self.name} повернул направо'

    def Show_Speed(self):
        return f'Скорость {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

    def Show_Speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Превышение скорости!!'
        else:
            return f'Движение с разрешенной скоростью!!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

    def Show_Speed(self):
        print(f'Текущая скорость {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Превышение скорости!!'
        else:
            return f'Движение с разрешенной скоростью!!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

    def police(self):
        if self.is_police:
            return f'{self.name} работает в Полиции'
        else:
            return f'{self.name} не работает в полиции'


porche = SportCar(100, 'Красный', 'Porche', False)
hundai = TownCar(30, 'Белый', 'Hundai', False)
ford = WorkCar(70, 'Розовый', 'Ford', True)
cadilac = PoliceCar(110, 'Голубой', 'Cadilac', True)
print(ford.Turn_Left())
print(f'Если {hundai.Turn_Rigth()}, то {porche.Stop()}')
print(f'{ford.Go()} обычной скоростью  {ford.Show_Speed()}')
print(f'{ford.name} был {ford.color}')
print(f'{porche.name} работает в Полиции? {porche.is_police}')
print(f'{ford.name}  работает в Полиции? {ford.is_police}')
print(porche.Show_Speed())
print(hundai.Show_Speed())
print(cadilac.police())
print(cadilac.Show_Speed())