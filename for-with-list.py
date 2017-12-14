b=0
a=input("Enter your name")
for i in a:
    if (i in ['A','E','I','O','U','a','e','i','o','u']):
        b=b+1
print ("You have",b,"vowels in your name")
input("Hit enter to exit")        
