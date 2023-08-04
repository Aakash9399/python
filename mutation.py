n_a=int(input())
A=set(map(int,input().split(" ")))
n_opr=int(input())
for i in range(n_opr):
    cmd=list(input().split(" "))
    temp=set(map(int,input().split(" ")))
    if cmd[0]=="intersection_update":
        A.intersection_update(temp)
    elif cmd[0]=="update":
        A.update(temp)
    elif cmd[0]=="symmetric_difference_update":
        A.symmetric_difference_update(temp)
    elif cmd[0]=="difference_update":
        A.difference_update(temp)

print(sum(A))
