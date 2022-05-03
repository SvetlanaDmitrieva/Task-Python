#30.Вычислить число  c заданной точностью d
#	Пример: при d = 0.001,  = 3.141. (10**(-10) < d < 10**(-1))
def pii(testexp=-10):
    M = 1.0
    denom = 2.0
    Pi = 3.0
    piPrevios=0.0
    for i in range(50000):
        delta = abs(Pi - piPrevios)
        if delta <= (10 ** (testexp)):
            return round(Pi,-testexp)  
        else:
            piPrevios=Pi
            Pi+=((4.0/(denom*(denom+1)*(denom+2.0)))*M)
            denom += 2.0
            M *= -1.0
accuracy=int(input('Введите точность d={10**(-10) < d < 10**(-1)} в интервале [-10,-1] для вывода числа Pi= '))
print(f'Pi = {pii(accuracy)}')
