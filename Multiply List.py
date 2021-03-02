import numpy
def Mul():
    lst=[]
    n=int(input('Enter the size: '))
    for i in range(n):
        a=int(input())
        lst.append(a)
    print('List:',lst)
    mul=numpy.prod(lst)
    print('Product: ')
    return mul
print(Mul())
