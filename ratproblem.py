def calculate (r, unit, arr, n):
    if n == 0:
        return -1 
        
    totalFoodRequired = r * unit 
    foodTillNow = 0 
    house = 0 
        
    for house in range (n):
        foodTillNow += arr[house] 
        if foodTillNow>=totalFoodRequired:
            break 
    if totalFoodRequired > foodTillNow:
        return 0
    return house + 1
	  
r = int(input("Enter value for r: "))
unit = int(input("Enter value for unit: "))
n = int(input("Enter the number of elements in arr: "))

arr = list(map(int, input("Enter space-separated values for arr: ").split()))
print(calculate(r, unit, arr, n))
