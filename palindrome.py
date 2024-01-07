

def isPalindrome(x):
    # convert the number in string
    num=str(x)
    # reverse the string
    rnum=num[::-1]
    # compare both
    return num == rnum
x=int(input("enter the number:"))

if isPalindrome(x):
    print("true")
else:
    print("false")
    
