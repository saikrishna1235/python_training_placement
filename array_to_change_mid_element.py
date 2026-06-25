#wap to read an array of ints and change the mid element to mid+1
from array import *
arr = array('i',[4,5,2,1,6,8,2])
for i in arr:
    print(i,end=' ')
print("")
# print(arr[3]+1)
mid=len(arr)//2;
# print(mid)
arr[mid]=arr[mid]+1
for i in arr:
    print(i,end=' ')