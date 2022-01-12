# Задание 3.9. Найти среднее арифметическое элементов списка

import random

listSize = int(input("Enter list size: \n"))
List = []
for i in range(listSize):
    a = random.randint(0, 100)
    List.append(a)

s = sum(List)
l = len(List)
a = s/l

print("List elements: ")
for i in range(listSize):
    print(List[i])

print("List average: "+str(a))

