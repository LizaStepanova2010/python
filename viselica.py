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
    wors = {'фрукты':'апельсин мандарин анас банан яблоко арбус дыня барбарис слива груша'.split(),
        'фигуры':'круг квадрат треугольник овал пятиугольник трапецыя ромб шестиугольник звезда'.split(),
        'цвета':'красный оранжавый желтый зеленый голубой синий фиолетовый белый коричневый'.split(),
        'животные':'аноконда акула белка быки гусь галка жаба журавль зебра змея индейка ирбис кабан кенгуру лама леопард мышь мартышка нанду насорог олень орел павлин панда ревун рысь сайгак скат тигр тюлень уж улитка филин хомяк цапля червяк щука ястеб ящерица'.split()}
    return wors 

def vyborSlova(spis,uS):
    if uS == 'Л':
        for i in range(len(list(spis.keys()))):
            print('Для выбора категории '+list(spis.keys())[i]+' ведите '+str(i))
        
        while True:
            katSlov = input()
            if not katSlov.isdigit():
                print('ввидите только цыфры')
            else:
                katSlov = int(katSlov)
                if katSlov > len(list(spis.keys())):
                    print('вы ввели неверное число')
                else:
                    break
        kategoriya = list(spis.keys())[katSlov]
    else:
        kategoriya = random.choice (list(spis.keys()))

    indexSlova = random.randint(0,len(spis[kategoriya])-1)
    return[spis[kategoriya][indexSlova],kategoriya]
def vyborUs():
    while True:
        print('Выберите уровень сложности')
        print('Выберите "Л" для легкого уровня')
        print('Выберите "С" для среднего  уровня')
        print('Выберите "Т" для трудного уровня')
        uroven = input ()
        uroven = uroven.upper() 
        if len (uroven) != 1:
            print('Надо вводить только один символ.')
        elif uroven not in 'ЛСТ':
            print('Надо вводить только Л,С или Т')
        else:
            return uroven


def proverka(strbukv):
    while True:
        print('Введите букву')
        buk = input()
        buk = buk.lower()
        if len(buk) != 1:
            print('Надо ввести только одну букву')
        elif buk not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Надо вводить только русские буквы')
        elif buk in strbukv:
            print('Вы уже назвали эту букву')
        else:
            return buk

def displayBoard(nasyVis,errorBuk,esBuky,sicretSl, urS, KS):
    if urS in 'ЛС':
        print(KS)
    print(nasyVis[len(errorBuk)])
    print()
    print('Ошибочные буквы:'+errorBuk)
    print()

    shablon = '_'*len(sicretSl)

    for i in range(len(sicretSl)):
        if sicretSl[i] in esBuky:
            shablon = shablon[:i]+sicretSl[i]+shablon[i+1:]

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
wordsS = genSlov()

strokaErrorB = ''
strokaYesB = ''
gameOver = False

urovenSL = vyborUs()
sicretSlovo,katSL = vyborSlova(wordsS,urovenSL)


while True:
    displayBoard(vis,strokaErrorB,strokaYesB,sicretSlovo,urovenSL,katSL)
    vvedenayaB = proverka(strokaErrorB+strokaYesB)

    if vvedenayaB in sicretSlovo:
        strokaYesB = strokaYesB + vvedenayaB

        konerGeme = True
        for i in range(len(sicretSlovo)):
            if sicretSlovo[i] not in strokaYesB:
                konerGeme = False
                break
        if konerGeme:
            print('ДА!Поздравляю!Секретная слово - '+sicretSlovo+'')
            gameOver = True 
    else:
        strokaErrorB = strokaErrorB + vvedenayaB

        if len(strokaErrorB)==len(vis)-1:
            displayBoard(vis,strokaErrorB,strokaYesB,sicretSlovo)
            print('''         Вы исчерпали все попытки!
            Назвоно ошибочных букв: '''+str(len(strokaErrorB))+'''
            угадоно букв:'''+str(len(strokaYesB))+'''
            было загадоно слово:'''+sicretSlovo+'.') 
            gameOver = True
    if gameOver:
        if playAqain():
            urovenSL = vyborUs()
            sicretSlovo,katSL = vyborSlova(wordsS,urovenSL)

            strokaErrorB = ''
            strokaYesB = ''
            gameOver = False
        else:
            break
            

            




