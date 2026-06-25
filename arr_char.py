from array import *
arr=array('u',input("Enter 10 char"))
for i in arr:
    print(i,end='')
for i in arr:
    if arr[i] == arr[i]+1:
        print(arr[i])
    else:
        print("No match")