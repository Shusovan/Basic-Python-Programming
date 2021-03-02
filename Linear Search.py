def linear_search():
    lst = []
 
    num = int(input("Enter size of list: "))
    print('Enter the elements')
    for n in range(num):
        numbers = int(input())
        lst.append(numbers)
    x = int(input("Enter number to search: "))
    found = False
    for i in range(len(lst)):
        if lst[i] == x:
            found = True
            print("%d found at position %d" % (x, i+1))
            break
    if not found:
        print("%d is not in list" % x)
print(linear_search())