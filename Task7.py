#Напишите программу, которая принимает на вход 
#число N и выдает набор произведений чисел от 1 до N.

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


print('Введите число: ')
n = int(input())
print(factorial(n))
