#37/Дан список чисел. Создать список в который попадают числа, описывающие возрастающую
#  последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
def outList(listA):
    counter=0
    while counter<=len(listA)-3:
        if listA[counter+2]>listA[counter]:
            if (listA[counter+1]>listA[counter]) and (listA[counter+2]>listA[counter+1]):
                counter+=1
            else:
                if counter ==0:
                    listA.pop(counter+1)
                else:
                    listA.pop(counter+2)
        else:
            if counter==0 :
                listA.pop(counter)
            else:
                listA.pop(counter+2)
    return listA
print('Введите список чисел :')
list01=list(map(int,input().split()))
# print(f'list01 = {list01}')
list02=list01.copy()
list03=[]
list03= outList(list02)
print(f'Получена возрастающая последовательность :{list03}')