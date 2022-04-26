#12.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
dictoinaryN=dict()
lenDictionary=int(input('Введите длину словаря индекс-значение:' ))
for i in range(1,lenDictionary+1):
    dictoinaryN[i]=3*i+1
print('Получен словарь индекс-значение : ')
print(dictoinaryN)
