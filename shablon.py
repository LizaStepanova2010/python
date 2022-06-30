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

def proverka(dengi,minStavka):
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
    
     
def sravnenie(game,igrok) :
    if game == igrok :            
        sovpdenie = True
    else:
        sovpdenie = False
        return sovpdenie
    
def intro2():  
    print('''яяяяяяя''')

def otvet():
    print('Введите номер наперсткка:')
    nap = input()
    while True:
        if nap.isdigit():
            if (nap in '123') and (len(nap)==1):
                nap = int(nap)
                break
            else:
                print('надо ввести только 1,2 или 3')
                nap = input()
        else:
            print('надо вводить цыфры')
            nap = input()
    return nap           
    
    
def playAqain():   
    # создаем бесконечный цикл

    # задаем вопрос и получаем ответ
     
    #  проверяем ответ на совподение со следуйщими фразами 
    # "да", "Да", "ДА", "д", "y", "yes", "Yes", "YES"
    # если есть совпадение то в переменой пресваеваем значение True
    
#  проверяем ответ на совподение со следуйщими фразами 
    # "нет", "Нет", "НЕТ", "н", "n", "no", "No", "NO"
    # если есть совпадение то в переменой пресваеваем значение false

    # если с первыми двумя случиями нет
    # говорим пользевателю, что не поняли его ответа     
    while True:
        print ('Хочешь ли ты поиграть еще?')
        guest =input()
        guest = guest.lower()
        if (guest =="да") or (guest =="д") or  (guest =="y") or (guest =="yes"):
       
 
            return True
        if (guest == "нет") or (guest == "н") or (guest == "n") or (guest =="no"):
            return False
        else:
            print('я не понял ответ.')



    
       

#
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
#


many,minBig = nastroyki()
intro()
while True:





    stavkaIgroka = proverka(many,minBig)
    napG = random .randint (1,3)
    napI = otvet() 
    if sravnenie(napG,napI) :
        print('Поздровляю! Ты выйграл.')
        many =  many + stavkaIgrka 
    print('Увы ты проиграл!')
    if many > minBig
    # задодим вопрос хочет ли человек сыграть еще
    if playAqain():
        print('Хорошо. У вас в наличии '+str(many)+'.Игра будет закончена')

        break
    else:
        print('у вас осталось денег меньше минимальной ставки')
        print('в наличии +str(many)  Игра будет завершена')
        break


