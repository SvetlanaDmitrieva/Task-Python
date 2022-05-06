#17.Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import random
# Заполнение списка из N элементов, заполненных числами из [-N, N]
setNumbers=int(input('Введите количество элементов списка (больше 0):'))
listNumbers=[]
for i in range(setNumbers):
    listNumbers.append(random.randint(-setNumbers, setNumbers))
print(f'listNumbers= {listNumbers}') #печать списка из N элементов
# Определение количества строк в файле file.txt
numberStrings=random.randint(2, setNumbers)
print(f'numberStrings= {numberStrings}') # печать количества строк в файле file.txt
# Формирование файла file.txt
with open('file.txt', 'w+') as f:
    for i in range(numberStrings):
        f.write(str(random.randint(0, setNumbers-1)) + '\n')
#Вычисление произведения элементов на указанных позициях
multiply=1
with open('file.txt', 'r') as f:
    for i in range(numberStrings):
        indexF=int(f.readline())
        readLine=listNumbers[indexF]
        multiply*=readLine
        print(f'index = {indexF} readLine = {readLine} multiply = {multiply}')
   