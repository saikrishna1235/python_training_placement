def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
nums=list(map(int,input().split()))
mid=len(nums)//2
fh=sum(nums[:mid])
sh=sum(nums[mid:])
if fh==sh:
    isprime(fh)
    print("Pizza")
else:
    print("False")