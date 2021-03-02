def odd_even():
    even_count=0
    odd_count=0
    lst=[]
    n=int(input('Enter the elements: '))
    for i in range(n):
        a=int(input())
        lst.append(a)
        if i%2==0:
            even_count+=1
        if i%2!=0:
            odd_count+=1
    print('Number of even: ',even_count)
    print('Number of odd: ',odd_count)
    return 
print(odd_even())