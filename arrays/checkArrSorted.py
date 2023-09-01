'''def arrSorted(arr, n):
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                return False 
            
    return False
'''

def arrSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

arr = [1,2,3,4,5,6]
n = len(arr)
j = arrSorted(arr, n)

if j:

    print("True")
else:
    print("False")