# Эту задачу взяла с видео семинара:
# Задайте список из n чисел последовательности (1+\n)^n 
# и выведите на экран их сумму.

n = int(input("Введите натуральное число: "))
posledovatelnost=[]
summa=0
for i in range(n):
    x=round((1+1/(i+1))**(i+1),2)
    posledovatelnost.append(x)
    summa+=x
print('Сумма = ',summa)
for i in range(len(posledovatelnost)):
     print(f"{i+1}: {posledovatelnost[i]}",end=",  ")
