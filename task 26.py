#26.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
 # Т е для k = 8, список будет выглядеть так:
 #  [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи      
def signF(numb):
    return (numb>0)-(numb<0)

def Fibb( numberF):
    if numberF in [-1,1,2]:
        return 1
    elif numberF==0:
        return 0
    else:
        sNum=int(signF(numberF))
        return (Fibb(sNum*(abs(numberF)-2))+sNum*Fibb(sNum*(abs(numberF)-1)))
list01=[]
numb=int (input('Введите число для составления списка Фибоначчи: '))
for e in range(numb+1):
    list01.append(Fibb(e))
for e in range(-1, (-1)*(numb+1),-1) :
    list01.insert(0,Fibb(e))
print(list01) 





