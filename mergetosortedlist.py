def merge_sorted_list(lst1,lst2):
    result=[]
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    result+=lst1
    result+=lst2
    return result
lst1=[1,2,3,4]
lst2=[4,5,6,7]

print(merge_sorted_list(lst1,lst2))