#empty set
empty_set=set()

var={1,2,3,1.3,"aakash"}
var1={4,56,6,"piyush"}

#union
var3=var.union(var1)
print(var3)
print(var)
#add a element
var.add("yassh")
print(var)

#pop
var.pop()
var.remove("aakash")
print(var)

var.clear()
print(var)
var1.discard("2")