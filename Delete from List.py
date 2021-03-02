def DeleteList():
    lst=[]
    k=int(input('Enter the size: '))
    for i in range(k):
        a=int(input())
        lst.append(a)
    n=int(input('Enter the number to remove: '))
    lst.remove(n)
    return lst
print(DeleteList())
    