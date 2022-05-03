#27.Строка содержит набор чисел. Показать большее и меньшее число
#Символ-разделитель - пробел
list01="247 33 568 41 149 995"
setNumbers=list01.split()
minNumber=int(setNumbers[0])
maxNumber=minNumber
for i in range(1,len(setNumbers)):
    numberFromSet=int(setNumbers[i])
    if numberFromSet > maxNumber:
        maxNumber= numberFromSet
    if numberFromSet < minNumber:
        minNumber= numberFromSet
print(f'Набор чисел - {list01} , минимальное= {minNumber}, максимальное= {maxNumber}')