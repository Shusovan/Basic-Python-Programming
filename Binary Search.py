def Binary_Search():

    arr=[]
    a=int(input('Enter the size: '))
    for i in range(a):
        n=int(input())
        arr.append(n)
    x=int(input('Enter the key: '))
    
    low=0
    high=len(arr)-1
    mid=0
    
    while low<=high:
           
        mid=(low+high)//2
        
        if x>arr[mid]:
            low=mid+1
            
        if x==arr[mid]:
            return mid
        
        if x<arr[mid]:
            high=mid-1
            
    return -1

index=Binary_Search()

if index>=0:
    print('The element is present at position: ',index+1)
else:
    print('Element is not present')
            
        
        
