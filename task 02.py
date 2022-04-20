#2.	Найти максимальное из пяти чисел
arrayNumbers=[]
for i in range(1,6):
     arrayNumbers.append(int(input(f'Введите {i} число из 5 =:')))
print('Максимальное значение из введенных чисел равно ', max(arrayNumbers))

