def Bubble_Sort(a):
    b=len(a)-1
    for i in range(b):
        for y in range(b-i):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
    return a

a=[]
n=int(input('Enter the size: '))
for j in range(n):
    num=input()
    a.append(num)
Bubble_Sort(a)

print('\nSorted array: ')
for i in range(n):
    print(a[i])
