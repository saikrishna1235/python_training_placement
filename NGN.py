li=[2,55,1,458,5,872,6,21,6,96,85,12,58,7822,68,93,1000,-1100,-52,0]
n=int(input("Enter the number :"))
for i in range(n+1,max(li)+1):
    if i in li:
        print(i)
        break
else:
    print(f"{n} itself greater")