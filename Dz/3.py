# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите натуральное число: "))
posledovatelnost=[]
summa=0
for i in range(n):
    x=(1+1/(i+1))**(i+1)
    posledovatelnost.append(x)
    summa+=x
print(posledovatelnost)
print(summa)