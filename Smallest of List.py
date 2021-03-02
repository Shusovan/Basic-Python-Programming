def SmallestofList():
    lst=[]
    n=int(input('Enter the size: '))
    for i in range(0,n):
        a=int(input())
        lst.append(a)
    lst.sort()
    print('Smallest element')
    return lst[0]
print(SmallestofList())