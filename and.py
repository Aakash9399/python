def AND(a,b):
    if(a==1 & b==1):
        return True
    elif(a==1 & b==0):
        return False
    elif(a==0 & b==1):
        return False
    elif(a==0 & b==0):
        return False

a=int(input("enter tha value of a"))
print(a)
b=int(input("enter the value of b"))
print(b)
c=AND(a,b)
print(c)