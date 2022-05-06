#16.Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
def sequenceF (num):
    if num<=0 :
        return print(f'Ошибка ввода: {num} - число не может быть меньше или равно 0')
    else:
        return (1+1/num)**num

sequenceNumber=int(input('Введите число - длину числовой посдедовательности (1+1/n)**n :'))
listSequence=[]
summSequence=0.0
if sequenceNumber>0 :
    for i in range(sequenceNumber):
        listSequence.append(sequenceF(i+1))
        summSequence+=listSequence[i]
    print(f'Список из {sequenceNumber} чисел последовательности: {listSequence}') 
    print (f'Сумма чисел полученной последовательности :{summSequence}')
else:
    sequenceF(sequenceNumber)