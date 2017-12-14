import random
counter=0
while True:
    input("Hit enter to roll the dice ")
    a=random.randint(1,6)
    if(a==6):
        print('you hit six')
        counter=counter+1
        print('You have hit a six in your',counter,'attempt.')
        break
    elif(a!=6):
        print('Hard luck, no six. You got',a,'.',end=" ")
        yesorno=input('Do you want to continue yes/no?: ')
        if(yesorno.lower()=='yes'):
            counter=counter+1
            continue
            print('You have hit a six in your',counter,'attempt.')
        elif(yesorno.lower()=='no'):
            exit()
        else:
            print('Wrong input')
            exit()
