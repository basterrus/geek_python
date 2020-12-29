# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
from colorama import init, Back, Fore

init()


class TrafficLigth:
    __color_name =  ['КРАСНЫЙ','ЖЕЛТЫЙ','ЗЕЛЕНЫЙ']

    def running(self):
        while True:
            print(Back.RED + f'{TrafficLigth.__color_name[0]} СВЕТ - 7 секунд')
            time.sleep(7)
            print(Back.YELLOW + f'{TrafficLigth.__color_name[1]} СВЕТ - 2 секунды')
            time.sleep(2)
            print(Back.GREEN + f'{TrafficLigth.__color_name[2]} СВЕТ - 10 секунд')
            time.sleep(10)


TrafficLigth = TrafficLigth()
TrafficLigth.running()

# Надеюсь правильно понял задание, ну и выпендрился с колорамой ))
