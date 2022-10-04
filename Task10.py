#Реализуйте алгоритм перемешивания списка.

import random


my_list = [6, 7, 8, 9, 10, 11]
result = []

for number in range(1000):
    i = random.randint(0, len(my_list)-1)
    if my_list[i] in result:
        i = random.randint(0, len(my_list)-1)   
    else:
        result.append(my_list[i])

print(result)
