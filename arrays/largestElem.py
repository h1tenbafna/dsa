'''

arr1 = [2,5,1,3,0]

arr1.sort()
b = arr1[-1]

'''
def findLargestElem(arr, n):
    maxi = arr[0]
    for i in range(0, n):
        if (maxi < arr[i]):
            maxi = arr[i]
    return maxi

arr = [2,5,1,3,0]
n = len(arr)

p = findLargestElem(arr, n)
print(p)

