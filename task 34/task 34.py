#34.Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.
def findAllIndexes(inputStr, searchStr):  
# формирование списка индексов вхождения searchStr в строке inputStr
    l1 = [] 
    length = len(inputStr) 
    index = 0 
    while index < length: 
        i = inputStr.find(searchStr, index) 
        if i == -1: 
            return l1 
        l1.append(i) 
        index = i + 1 
    return l1
#--------------------------------------------
def sortKey(sortD): 
    return sortD[1]
#--------------------------------------------
def findValue(value, seq):
    for index, item in enumerate(seq):
        if value in item: 
              return index, item
    return -1, item
#--------------------------------------------
def shareString(stringSum):
# формироваине в виде списка коэффициентов и степеней одночленов многочлена
    lSumbol=[]
    sumbolX=max(stringSum.find('x'),stringSum.find('X'),stringSum.find('х'),stringSum.find('Х'))
    if sumbolX==-1:
        lSumbol.append(int(stringSum))
        lSumbol.append('0')
        return lSumbol
    coefficient=int(stringSum[0:sumbolX])
    numEnd=stringSum.find('**')
    if (numEnd!=-1):
        lSumbol.append(coefficient)
        lSumbol.append((stringSum[numEnd+2:]))
        return lSumbol
    numEnd=stringSum.find('^') 
    if (numEnd!=-1):
        lSumbol.append(coefficient)
        lSumbol.append((stringSum[numEnd+1:]))
        return lSumbol
    lSumbol.append(coefficient)
    lSumbol.append('1')
    return lSumbol
#---------------------------------------------------
stringFile=[]
listFiles=['file01.txt','file02.txt']
listPlus=[]
listMinus=[]
allPolynomial=[]
for i in range(2):
    fileS=open((listFiles[i]),'r')  #открытие файлов для чтения многочленов
    stringFile.append(str(fileS.readline()))
    print(f'строка многочлена {i+1} = {stringFile[i]}')
    j=str(stringFile[i]).find('=')
    if j!=-1:
        stringFile[i]= stringFile[i][:j] # обрезание конца строки, начиная с подстроки '="
    fileS.close()
    listPlus=findAllIndexes(str(stringFile[i]),'+')  #формирование списка позиций разделителей '+' и '-' строки многочлена 
    listMinus=findAllIndexes(str(stringFile[i]),'-') #виде списка списков [коэффициент, степень одночлена]
    listPlus.extend(listMinus)
    listPlus.sort()
    listPlus.append(len(stringFile[i])) # сортировк списка и добавления индекса последнего символа строки многочлена
    polynomial=list()
    minIndex=0
    for j in range(len(listPlus)): #формирование списка списков [коэффициент, 'степень одночлена'] многочленов
        maxIndex=int(listPlus[j])
        polynomial.append(shareString(str(stringFile[i][minIndex:maxIndex])))
        minIndex=maxIndex
    polynomial.sort(key=sortKey,reverse=True) #сортировка списка по 'степень одночлена' по убыванию
    listPlus.clear()
    listMinus.clear()
    allPolynomial.append(polynomial) # объединение списков одночленов каждого многочлена в один список
maxIndex=max(allPolynomial[0][0][1],allPolynomial[1][0][1]) # выяснение максиммальной степени многочленов
polynomialFormula=''
for i in range(int(maxIndex),-1,-1):
    coefficient=0.0
    for j in range (2):
        index,findCoef=findValue(str(i),allPolynomial[j])  # поиск коэффициентов для каждой степени
        if index!=-1:
            coefficient+=findCoef[0]                       # сложение коэффициентов одночленов равной степени
    if coefficient!=0.0:
        if  i!=int(maxIndex) and coefficient>0 :
            polynomialFormula+='+'
        if i==0:
            polynomialFormula+=str(coefficient)
        else :
            if coefficient==-1.0 : 
                polynomialFormula+='-'
            if abs(coefficient) !=1.0:
                polynomialFormula+=str(coefficient)
        if i!=0:
            polynomialFormula+="x"
        if i>1 :
            polynomialFormula+="^"+str(i)
polynomialFormula+=' = 0'
print(f'сумма многочленов = {polynomialFormula}') # запись строки суммы многочлена в новый файл
fileS=open('file03.txt','w')
fileS.write(polynomialFormula)
fileS.close()