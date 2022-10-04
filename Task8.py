# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

def my_range(n):
    result = []
    for i in range(1, n + 1):
        result.append((1 + 1 / n) ** n)
    return result


def final_sum(result_list):
    sum = 0
    for number in result_list:
        sum += number
    return sum


print('Введите число: ')
n = int(input())
print(round(final_sum(my_range(n)), 3))
