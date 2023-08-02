n = int(input("enter the number of element :"))
s = set(map(int, input().split()))

opr=int(input("enter the number of operation"))

for i in range(opr):
    command=input()
    
    com_list=list(command.split(" "))
    if com_list[0]=='remove':
        s.remove(int(com_list[1]))
    elif com_list[0]=='pop':
        s.pop()
    elif com_list[0]=='discard':
        s.discard(int(com_list[1]))
        
print(sum(s))
        