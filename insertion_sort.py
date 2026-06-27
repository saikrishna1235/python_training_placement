def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while(j>=0 and key<l[j]):
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
    print(l)
x=[10,9,8,7,6,5,4,3,2,1]
insertion_sort(x)