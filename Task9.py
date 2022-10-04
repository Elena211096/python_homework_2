#Задайте список из N элементов, заполненных числами из промежутка [-N, N]
#Найдите произведение элементов на позициях a и b.
#Значения N, a и b вводит пользователь с клавиатуры.


def my_range(n):
    result = []
    for i in range (-n, n + 1):
        result.append(i)
    return result


print('Введите число N: ')
N = int(input())
print(my_range(N))
my_list = my_range(N)
print('Введите позицию a: ')
a = int(input())
print('Введите позицию b: ')
b = int(input())


print(my_list)
answer = 0
answer = my_list[a-1]*my_list[b-1]
print(answer)
