import random
a=random.randint(1,20)
while True:
    b=int(input("Guess the number"))
    if (b < a):
        print("You have entered less")
    elif(b > a):
        print("You have entered greater")
    else:
        print("You have guessed it right. It's",b)
    continue

