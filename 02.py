import random
while True:
    x = random.randint(1,10)
    print("Мы загадали число от 1 до 10, сможешь отгодать?")
    for i in range(3):
        z = input()
        z = int(z)

        if x > z:
            print('загадонное число больше')
        if x<z:    
            print('загадонное число меньше')
        if x==z:
            break

    if x==z:
        print('Поздравляю.')
    if x != z:
        print("Увы, загаданное число "+str(x))

    pr = True
    print('ты хочешь попробовать еще один раз?')
    otvet=input()
    if (otvet=='да') or (otvet=='д') or (otvet =='yes') or (otvet == 'y'):
        pr = False
    if pr:
        break    
