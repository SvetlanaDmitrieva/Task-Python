#18.Реализовать алгоритм перемешивания списка. 
import random
setNumbers=int(input('Введите количество элементов списка (больше 0):'))
listNumbers01=[]
listNumbers02=[]
for i in range(setNumbers):
    listNumbers01.insert(0,random.randint(-setNumbers, setNumbers))
    listNumbers02.insert(0,listNumbers01[0])

for i in range(setNumbers-1, 0, -1):
    j = random.randint(0, i + 1) 
    listNumbers02[i], listNumbers02[j] = listNumbers02[j], listNumbers02[i] 
print (f"Исходный список : {listNumbers01}")
print (f"Перемешанный список : {listNumbers02}")