#23.	Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]         
list01=[2, 3, 4, 5, 6,7,8]
list02=[]
lenList01=len(list01)
middleList01=lenList01//2
for i in range(middleList01):
    list02.append(list01[i]*list01[lenList01-1-i])
if (lenList01%2!=0):
    list02.append(list01[middleList01]**2)
print(f'Список произведений пар чисел в списке: {list02}')
print(f'Исходный список пар чисел :{list01}')
