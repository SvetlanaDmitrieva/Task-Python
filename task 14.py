#14.Подсчитать сумму цифр в вещественном числе.
number = input("Введите вещественное число: ")
number01 = number.replace(',','.') 
listN=number01.split('.')
number02=listN[0]+listN[1] 
sumNumbers=0
for val in number02:
      sumNumbers+= int(val) 
print(f'Сумма цифр введенного числа {number01} равна = {sumNumbers}')
