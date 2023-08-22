def selectionSort(a, n):
    for i in range (0, n-1):
        mini = i
        for j in range(i+1, n):
            if a[j] < a[mini]:
                mini = j
                
        a[mini], a[i] = a[i], a[mini]
    
    for k in range(0, n):
        print(a[k])
        
a= [13, 46, 24, 52, 20, 9]
n = len(a)

h = selectionSort(a, n)
        