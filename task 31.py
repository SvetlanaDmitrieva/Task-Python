#31.Составить список простых множителей натурального числа N
import math 
def multiplierList(num): 
    listMultiplier=[]
    while num % 2 == 0: 
       listMultiplier.append(2)
       num = num / 2 
    for i in range(3, int(math.sqrt(num)) + 1, 2): 
         while num % i == 0: 
            listMultiplier.append(i)
            num = num / i 
    if num > 2: 
        listMultiplier.append(num)
    return listMultiplier
num = int(input('Введите натуральное число для получения списка простых множителей : '))
print (f'Список простых множителей = {multiplierList(num)}') 
