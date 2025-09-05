
def second_largest(arr):
    
    arr = set(arr)
    
    if len(arr) < 2:
        return 
    
    largest = second = -9999999
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num
    return second



#n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

print("Second largest:", second_largest(arr))