#19.Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

import time
def randomNumber(minimum, maximum):
    now=str(time.time())
    rnd=float(now[::1][13:16:])/1000
    return int(minimum+rnd*(maximum-minimum))
print (randomNumber(0,1000))