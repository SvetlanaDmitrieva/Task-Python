#24.В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением 
# дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19    
list01=  [1.85, 1.3, 3.1, 5, 10.01, 5.005]
minFractionalPart =1.0
maxFractionalPart =0.0
for i in range(len(list01)):
    fractionalPart=round(list01[i]%1.0,3)
    if (fractionalPart<minFractionalPart and fractionalPart!=0.0):
        minFractionalPart=fractionalPart
    if fractionalPart>maxFractionalPart:
        maxFractionalPart=fractionalPart
print(f'Разница между максимальным и минимальным значением ')
print(f'дробной части элементов списка равна {maxFractionalPart-minFractionalPart}')
#print(f'Исходный список вещественных чисел: {list01}')