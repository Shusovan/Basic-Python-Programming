lst=[]

def enqueue():
    n=input('Enter the elements of Queue: ')
    lst.append(n)
    menu()

def dequeue():
    lst.pop(0)
    menu()
    
def display():
    print(lst)
    menu()
    
def menu():
    print('\n*****MENU*****')
    print('1.Enqueue\n2.Dequeue\n3.Display\n4.Exit')
    choice=int(input('Enter your choice: '))
    if(choice==1):
        enqueue()
    elif(choice==2):
        dequeue()
    elif(choice==3):
        print('Current Queue: ')
        display()
    elif(choice==4):
        exit()
    else:
        print('Enter correct option')
        menu()
menu()
