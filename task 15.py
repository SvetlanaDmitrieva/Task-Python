#15.Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда  [ 1, 2, 6, 24 ]
numberSet=int(input('Введите длину набора произведений чисел:'))
listSet=[]
listSet.append(1)
for i in range(1,numberSet):
    listSet.append(listSet[i-1]*(i+1))
print (f'Получен следующий набор произведений для чисел от 1 до {numberSet}:')
print(listSet)  
