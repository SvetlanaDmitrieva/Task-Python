#5.	Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
numb=int(input('Введите число :'))
if (numb%5==0) and (numb%10==0):
    print('Введенное число кратно 5 и 10')
else:
   print('Введенное число не кратно одновременно 5 и 10') 
if (numb%15==0):
    if (numb%30!=0):
        print('Введенное число кратно 15 но не 30')
    else:
        print('Введенное число кратно одновременно 15 и 30')
else:
   print('Введенное число не кратно одновременно 15 и 30') 