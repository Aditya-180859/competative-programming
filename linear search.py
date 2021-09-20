n = int(input("enter number of array in list: "))
arr=[]

print("enter the element:")
for i in range(n):
    a=int(input())
    arr.append(a)

b = int(input("enter the element to search"))

flag=1
c=0
for i in arr:

    c += 1
    if (i==b):
        flag=0
        pos=c


if flag==0:
    print("element at found at ",pos)

else:
    print("element not found")