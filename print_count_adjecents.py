count=0
l=[1,2,4,4,5,6,6,9,9,1]
n=[]
i=0
for i in range(len(l)):
    if l[i]==l[i-1]:
        n.append(l[i])
        count+=1
print(count)
print(n)