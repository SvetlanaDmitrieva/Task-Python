#3.	Вывести на экран числа от -N до N
numbersN =int(input('Введите число N, определяющее интервал [-N,N]:'))
if abs(numbersN)!=0: 
       for i in range(-abs(numbersN),abs(numbersN)+1):
            print (f'{i}',end = " ")
else: 
        print('Введено значение 0. Повторите запуск программы')
   