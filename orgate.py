def OR(a,b):
    if(a==1 & b==1):
        return True
    elif(a==1 & b==0):
        return True
    elif(a==0 & b==1):
        return True
    elif(a==0 & b==0):
        return False
    
a=int(input("enter tha value of a"))
print(a)
b=int(input("enter the value of b"))
print(b)
c=OR(a,b)
print(c)