#
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
#
import random
#
#РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
#

# функция настроек
def nastroyki():
    print('ИГРА "НАПЕРСТКИ"')
    print()
    print('АВТОР: Степанова Лиза')
    print()
    print('версия 1.0')
    print()
    print ('Введите сколько денег у игрока денег')
    dengi = input()
    while True:
        if dengi.isdigit():
            dengi = int(dengi)
            break
        else:
            print('Надо вводить только цыфры')
            dengi = input()

    print('Введите размер минимальной ставки')
    minStavka = input()
    while True:
        if minStavka.isdigit():
            minStavka = int(minStavka)
            break
        else:
            print('Надо вводить только цыфры')
            minStavka = input()

    return [dengi,minStavka]

def intro():
    print('Шел один человик на рынок,и сидел один без породуктов')
    print()
    print('но у него было 3 наперстка и маленький шарик.')
    print
    print('Ему захотелось подойти к человеку и он рещает проверить свою удачу и сыграть на деньги. ')
    print()
    print('Человек начал играть, помоги ему')

def proverka (dengi,minStavka):
    print('сделайте вашу ставку')
    stavka  = input()
    while True:
        if stavka.isdigit():
            # переводи в строку число
            stavka = int (stavka)
            #проверяем что ставка больше минимальной 
            if stavka > minStavka:
                if stavka > dengi:
                    print('ставка не может быть больше суммы денег игрока') 
                    stavka = input()
                else:
                    break
            else:    
                print('ставка не может быть меньше минимальной') 
                stavka = input()
        else:
            print('надо вводить только цыфры')
            stavka = input()

    return stavka        

#
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
#

many,minBig = nastroyki()
intro()
stavkaIgroka = proverka(many,minBig)            
