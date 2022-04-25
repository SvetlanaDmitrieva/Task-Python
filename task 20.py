#20.Определить, присутствует ли в заданном списке строк, некоторое число  #
list=['1','123' ,'3256', '1254']
num='123'
chetchik=-1
for i in range(len(list)):
    if  num== list[i]:
        chetchik=i
        break
if chetchik == -1:
    print(f' Число {num} отсутствует в заданном списке строк :')
   
else:
    print(f' Число {num} присутствует (позиция {chetchik})в заданном списке строк:')
print(list)



