#43.Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
list01=[1,5,2,6,2,3,4,5,10]
list02=list(filter(lambda x: list01.count(x)==1,list01 ))
print(f'исходная последовательность  : {list01}')
print(f'уникальные элементы : {list02}')