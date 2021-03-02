def Quick_Sort(arr,low,high):
    if high-low>1:
        pivot=Partition(arr,low,high)
        Quick_Sort(arr,low,pivot)
        Quick_Sort(arr,pivot+1,high)
        
def Partition(arr,low,high):
    pivot=arr[low]
    i=low + 1
    j=high - 1
    
    while True:
        while i<=j and arr[i]<=pivot:
            i=i+1
        while i<=j and arr[j]>=pivot:
            j=j-1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            arr[low],arr[j]=arr[j],arr[low]
            return j

arr=[]
n=int(input('Enter the size: '))
for i in range(n):
    num=input()
    arr.append(num)

Quick_Sort(arr,0,len(arr))
print('Sorted Array: ')    
print(arr)