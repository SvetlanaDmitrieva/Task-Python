#11.Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.
numberList=int(input('Введите число членов последователбности: '))
list01=[]
member=1
for i in range(numberList):
    list01.append(member)
    member*=(-3)
print(f'Список из {numberList} членов :')
print(list01)


