#29.Найти НОК двух чисел
A=int(input('Введите первое число a= '))
B=int(input('Введите второе число b= '))
numA, numB=A,B
if numA<numB :
    numA, numB=numB,numA
while numB!= 0:
    numA,numB=numB, numA%numB
else:
    nod=numA
nok=A*B//nod
print(f'НОК чисел {A} и {B} равно {nok}')
