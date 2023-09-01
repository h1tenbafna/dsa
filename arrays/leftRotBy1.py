def solve(arr):
    
    return arr[1 : len(arr)] + arr[0:1]


arr = [1, 2, 3, 4, 5]
k = solve(arr)
print(k)
