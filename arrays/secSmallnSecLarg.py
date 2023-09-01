'''def getElems(arr, n):
    if n==0 or n==1:
        print(-1,-1)
    arr.sort()
    small = arr[1]
    large = arr[n-2]
    print("second smallest", small)
    print("sec largest", large)'''
    
    
#better
def getElems(arr, n):
    if n==0 or n==1:
        print(-1,-1)
    small = float('inf')
    sec_small = float('inf')
    large = float('-inf')
    sec_large = float('-inf')
    
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
        
    for i in range(n):
        if arr[i] < sec_small and arr[i] != small:
            sec_small = arr[i]
        if arr[i] > sec_large and arr[i] != large:
            sec_large = arr[i]
            
    print(sec_large)
    print(sec_small)

    

arr = [1,2,4,6,7,5]
n = len(arr)
getElems(arr, n)


#can be done in two functions 