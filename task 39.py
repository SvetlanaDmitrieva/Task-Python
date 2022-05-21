#39.Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры 
# человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 
import random
def playWithBot():
    rest=sweets=201
    flag=0
    while rest >0:
        print(f' Конфет = {rest}')
        while True: 
            if flag ==0:
                player=int(input(f'Ход игрока {(flag+1)} :'))
                if player > 28 or player > rest:
                    print (f'Превышено допустимое значение конфет ({min(rest,28)}), повторить ход')
                    continue
                else:
                    break
            else:
                if rest > 28:
                    player=random.randint(1,28)
                else:
                    player=rest
                print(f'Ход бота :{player}')
                break
        flag=(flag+1)%2
        rest-=player
    if flag==0: 
        print (f'Выиграл  бот')
    else:
        print (f'Выиграл  игрок')
    return

def playWithMan():
    rest=sweets=201
    flag=0
    while rest >0:
        print(f' Конфет = {rest}')
        while True: 
            player=int(input(f'Ход игрока {(flag+1)} :'))
            if player > 28 or player > rest:
                print (f'Превышено допустимое значение конфет ({min(rest,28)}), повторить ход')
                continue
            else:
                break
        flag=(flag+1)%2
        rest-=player
    if flag==0: flag=2
    print (f'Выиграл {(flag)} игрок:')
    return

game=int(input(f'Введите 1 (если ходите играть с человеком), 2 (если хотите играть с ботом) :'))
if game ==1 :
    playWithMan()
else:
    playWithBot()
