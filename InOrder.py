class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.parent=val
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)
root.right.left=Node(7)

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.parent)
        InOrder(root.right)

def PreOrder(root):
    if root:
        print(root.parent)
        PreOrder(root.left)
        PreOrder(root.right)
        
def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.parent)
        
def menu():
    print('*****MENU*****')
    print('1.InOrder\n2.PreOrder\n3.PostOrder\n4.Exit')
    choice=int(input('Enter your choice: '))
    
    if choice==1:
        print('InOrder:')
        InOrder(root)
    
    elif choice==2:
        print('PerOrder:')
        PreOrder(root)
        
    elif choice==3:
        print('PostOrder:')
        PostOrder(root)
        
    elif choice==4:
        Exit()
        
    else:
        print('Enter correct option')
        menu()
menu()