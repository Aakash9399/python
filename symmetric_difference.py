n_eng=int(input("enter the number"))


english=set()
french=set()

for i in range(n_eng):
    english.add(int(input("enter the number of student")))

n_french=int(input("enter the number"))
for j in range(n_french):
    french.add(int(input("enter the numbe of student")))
res=english.symmetric_difference(french)  
print(len(res))