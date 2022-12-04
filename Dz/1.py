# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

a = input("Введите вещественное число: ")
summa=0
new_a=a.translate({ord(i): None for i in '-'})
a=new_a.translate({ord(i): None for i in '.'})

for i in range(len(a)):
    b=int(a[i])
    summa+=b
print(summa)

# Решение от преподавателя

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))