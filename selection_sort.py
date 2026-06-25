lis=[5,4,2,9,8,2,1]
for i in range(len(lis)):
    min_index=i
    for j in range(i+1,len(lis)):
        if lis[j] < lis[min_index]:
            min_index=j
    lis[i],lis[min_index] = lis[min_index],lis[i]
print(lis)