#22.	Найти сумму чисел списка стоящих на нечетной позиции  
listNumbers=[25.55,64.85,97.32,35.15, 49.64,88.57,5.66, 11.43]   
sumNumbers=0.0
for i in range(len(listNumbers)):
    if i%2!=0:
        sumNumbers+=listNumbers[i]
print(f'Сумма чисел, стоящих на нечетной позиции, равна :{sumNumbers}')
print(listNumbers)
