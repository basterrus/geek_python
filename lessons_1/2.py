# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите \
# в формате чч:мм:сс. Используйте форматирование строк.

time_sec = int(input('Введите время в секундах: '))


def sec_to_time():
    h = time_sec // 3600
    m = time_sec % 3600 // 60
    s = time_sec % 3600 % 60
    res = f'{h}:{m}:{s}'
    return res


print(sec_to_time())
