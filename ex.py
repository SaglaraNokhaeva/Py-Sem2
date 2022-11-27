# Стоимость строки
# Дана строка текста. Напишите программу для подсчета стоимости строки,
# исходя из того, что один любой символ (в том числе пробел) стоит 
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести стоимость строки.

# Тестовые данные
# Sample Input 1:
# Привет, как дела?!
# Sample Output 1:
# 10 р. 80 коп.
# Sample Input 2:
# Тимур - лучший математик на свете!!
# Sample Output 2:
# 21 р. 0 коп.
text_string=input("Введите текст: ")
length_text_string=len(text_string)
cost=length_text_string*60
print(f"длина текста {cost}")
print(f"стоимость текста {cost//100} руб. и {cost%100} коп.")