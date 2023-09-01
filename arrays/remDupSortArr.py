
'''
def remDup(arr):
    s = set()
    for i in range(len(arr)):
        s.add(arr[i])
    k = len(s)    
    j = 0
    for x in s:
        arr[j] = x
        j+=1
    return k

'''

def remDup(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return i+1

arr = [1,1,2,2,3,3]
k = remDup(arr)
for i in range(k):
    print(arr[i], end = " ")