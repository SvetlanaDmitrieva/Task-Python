#13.Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
string01="белая березка стояла, белая кудрявая стояла, люли-люлю стояла, люли-люли стояла"
string02="стояла"
lenStr01=len(string01)
lenStr02=len(string02)
counter=0
i=0
while(i!=-1):
    i=string01.find(string02, i, lenStr01)
    if i!=-1 :
        counter+=1
        i+=lenStr02
if counter==0:
    print(f'В строке "{string01}" строка "{string02}" не найдена')
else:
    print(f'Найдено {counter} вхождений  строки "{string02}" в строку "{string01}"') 
