def AllEveninList():
    n=int(input('Start: '))
    m=int(input('End: '))
    for i in range(n,m+1):
        if i%2==0:
            print('The odd numbers is: ',i)
    return 
print(AllEveninList())