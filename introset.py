def average(array):
    heights=set(array)
    sum=0
    for item in heights:
        sum+=item
    avg=sum/len(heights)
    
    return avg
    

# n = int(input())
# arr = list(map(int, input().split()))
arr=[161,182,161,154,176,170,167,171,170,174]
result = average(arr)
print(result)