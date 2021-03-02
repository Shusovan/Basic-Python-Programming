def LargestofList():
    lst=[]
    n=int(input('Enter the size: '))
    for i in range(0,n):
        a=int(input())
        lst.append(a)
    num=[i for i in lst if i%2!=0]
    print('The even numbers are: ')
    return num
print(LargestofList())