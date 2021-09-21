n = int(input("enter number of array in list: "))
arr=[]

print("enter the element:")
for i in range(n):
    a=int(input())
    arr.append(a)

search = int(input("enter the element to search"))

flag=1
c=0

a=arr[0]
b=arr[n-1]

while(a<b):
    mid = n // 2
    if(arr[mid]==search):
        print("found at",mid+1)
        break

    elif(arr[mid]>search):
        b=arr[n-1]

    elif(arr[mid]>search):
        a=arr[n+1]
     
    else:
        print("not found")
