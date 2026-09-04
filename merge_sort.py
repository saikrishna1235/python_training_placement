def Merge_sort(ls):
    l=0
    m=(l+(len(ls)-1))//2

    left = ls[:m]
    right = ls[m+1:len(ls)]

    Merge_sort(left)
    Merge_sort(right)

    i,j,k = 0,0,0
    l1=[]
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            l1.append(left[i])
            i+=1
        else:
            l1.append(right[j])
            j+=1
        k+=1

        l1.extend(left)
        l1.extend(right)
    print(l1)
x=[10,9,8,7,6,5,4,3,2,1]
Merge_sort(x)
        