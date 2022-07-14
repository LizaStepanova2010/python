#
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
#
import random
#
#РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
#
def genVis():
    HANGMAN_PICT = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    0   |
        |
        |
       ===''','''
    +---+
    0   |
    |   |
        |
       ===''','''
    +---+
    0   |
   /|   |
        |
       ===''','''
    +---+
    0   |
   /|\  |
        |
       ===''','''
    +---+
    0   |
   /|\  |
        |
       ===''','''
    +---+
    0    |
   /|\   |
   /     |
       ===''','''
    +---+
    0    |
   /|\   |
   / \   |
       ===''']
    return HANGMAN_PICT

def genSlov():
    wors = ['аноконда акула белка быки гусь галка жаба журавль зебра змея индейка ирбис кабан кенгуру лама леопард мышь мартышка нанду насорог олень орел павлин панда ревун рысь сайгак скат тигр тюлень уж улитка филин хомяк цапля червяк щука ястеб ящерица'.split()]
    return wors
def vyborSlova(spis):
    indSl = random.randind(0,len(spis)-1)
    slovo = spis[indSl]
    return slovo 

def proverka(strbukv):
    while True:
            print('Введите букву')
            buk = input
            buk = buk.lower()
            if len(buk) != 1:
                print('Надо ввести только одну букву')
            elif buk not in 'йцукенгшщзхъфывапролджэячсмитьбю':
                print('Надо вводить только русские буквы')
            elif buk in strbukv:
                print('Вы уже назвали эту букву')
            else:
                return buk

def displayBoard(nasyVis,errorBuk,esBuky,sicretSl):
    print(nasyVis[len(errorBuk)])
    print()
    print('Ошибочные буквы:'+errorBuk)
    print()

    shablon = '_'*len(sicretSl)

    for i in range (len(sicretSl)):
        if sicretSl(i) in esBuky:
            shablon = shablon[:1]+sicretSl[:1]+shablon[i+1:]

    for s in shablon:
        print(s,end=' ')
    print()

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

vis = genVis()
wordsS = genSlov
sicretSlovo = vyborSlova(wordsS)
strokaErrorB = ''
strokaYesB = ''

while True:
    displayBoard(vis,strokaErrorB,strokaYesB,sicretSlovo)
    vvedenayaB = proverka(strokaErrorB+strokaYesB)


