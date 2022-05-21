#38.Напишите программу, удаляющую из текста все слова содержащие "абв".
string01 = str(input('Введите последовательность слов, содержащие в том числе "абв" :'))
list01 = string01.split()
list02=list(filter(lambda x : not 'абв' in x, list01))
string02 = (",".join(map(str, list02)))
print(string02)