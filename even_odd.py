le=[]
lo=[]
nums=list(map(int,input("Enter the numbers :").split()))
for i in nums:
    if i%2==0:
        le.append(i)
    else: 
        lo.append(i)
print(le,lo)