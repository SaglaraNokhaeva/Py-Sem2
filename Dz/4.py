# Реализуйте алгоритм перемешивания списка

import random
spisok=[]
n = int(input("Введите размерность списка: "))
for i in range(n):
    spisok.append(i)
print(spisok)
random.shuffle(spisok)
print(spisok)