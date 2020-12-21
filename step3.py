# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    nums = [a, b, c]
    nums.remove(min(nums))
    summa = nums[0] + nums[1]
    return summa


print(my_func(
    a=int(input('Введите число -a: ')),
    b=int(input('Введите число -b: ')),
    c=int(input('Введите число -b: ')),
))
