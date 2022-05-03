#33.Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
degreeNat=int(input('Введите натуральную степень многочлена  :'))
listDegree=[]
polynomial=""
for i in range(degreeNat+1):
    listDegree.insert(0,random.randint(0, 100))
for i in range(degreeNat+1):
    if listDegree[i]!=0:
        if listDegree[i]==1:
             strList=""
        else:
            strList=str(listDegree[i])
        if i == (degreeNat-1):
            polynomial+= strList + "x" + "+" 
        elif i == (degreeNat):
            polynomial+= strList  
        else:
            polynomial+= strList + "x^" + str(degreeNat-i)+ "+" 
    else:
        if i==degreeNat:
            polynomial= polynomial[:-1]
polynomial+="= 0 \n"
#print(f'Коэффициенты многочлена : {listDegree}, степень K= {degreeNat}')
print(polynomial)
file=open('filePython.txt','a')
file.write(polynomial)
file.close()
