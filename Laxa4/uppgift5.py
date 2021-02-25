import random
num = random.randint(1, 100)
while True:
    print('Gissa ett nummer mellan 1 och 100: ')
    gissa = input()
    i = int(gissa)
    
    if i == num:
        print('Du gissa rätt!!!')
        break
    elif i < num:
               print('Gissa på ett högre tal')
    elif i > num:
               print('Gissa på ett lägre tal') 

