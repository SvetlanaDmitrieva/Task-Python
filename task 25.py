#25. Написать программу преобразования десятичного числа в двоичное    

numberDecimal=int(input('Введите число для перевода в двоичную систему исчисления: '))
rest=numberDecimal
numberBinary=""
while (rest>0):
    numBin=rest%2
    rest//=2
    numberBinary=str(numBin) + numberBinary
print(f'Десятичное число {numberDecimal} в двоичной системе исчисления равно {numberBinary} ')