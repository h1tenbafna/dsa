def bubble_sort(n, a):
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                
        if swapped == False:
            break

a = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(len(a), a)
for i in range(len(a)):
    print("%d" % a[i], end= " ")
