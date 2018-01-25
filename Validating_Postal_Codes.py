
"""A postal code  must be a number in the range of (100000,999999).
A postal code  must not contain more than one alternating repetitive digit pair. 
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them."""

for i in range (100000,999999):
    a=list(str(i))
    count=0
    if(a[0]==a[2]):
        count=count+1
    if(a[1]==a[3]):
        count=count+1
    if(a[2]==a[4]):
        count=count+1
    if(a[3]==a[5]):
        count=count+1        
    if(count > 1):
        print(i,"is not valid")
    else:
        print(i,"is valid")
