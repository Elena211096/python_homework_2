# Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр


print('Введите число: ')
number = input()
result = 0


for i in range(len(number)):
    if number[i].isdigit():
        result += int(number[i])
print(result)
