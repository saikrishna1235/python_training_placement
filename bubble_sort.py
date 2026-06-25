lis=[2,5,6,1,3,4]
for i in range(len(lis)):
    for  j in range(len(lis)-1):
        if lis[j]>lis[j+1]:
            lis[j],lis[j+1] = lis[j+1],lis[j]
print(lis)