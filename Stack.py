lst=[]

def insert():
    n=input('Push values in stack: ')
    lst.append(n)
    menu()

def delete():
    lst.pop()
    menu()

def display():
    print(lst)
    menu()    

def menu():
    print('\n*****MENU*****')
    print('1.Push\n2.Pop\n3.Display\n4.Exit')
    choice=int(input('Enter your choice: '))
    if(choice==1):
        insert()
    elif(choice==2):
        delete()
    elif(choice==3):
        print('Current Stack: ')
        display()
    elif(choice==4):
        exit()
    else:
        print('Enter correct option')
        menu()
menu()
