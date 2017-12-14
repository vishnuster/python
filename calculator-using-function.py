def calculator(a,b):
    print ("addition",a+b)
    print ("substraction",a-b)
    print ("multiplication",a*b)
    print ("division",a/b)
    return
while True:
    try:
        a=float(input ("enter value for a"))
    except ValueError:
        print ("INVALID INPUT")
        continue
    else:
        break
while True:
    try:
        b=float(input ("enter value for b"))
    except ValueError:
        print ("INVALID INPUT")
        continue
    else:
        break
calculator(a,b)
input ("hit enter to exit")


