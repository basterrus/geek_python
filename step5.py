# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_umerals():
    nums = []
    while True:
        input_nums = input('Введите числа через пробел: ').split()
        for numeral in input_nums:
            if numeral == 'no':
                print(sum(nums))
                return
            nums.append(int(numeral))
        print(sum(nums))


sum_umerals()
