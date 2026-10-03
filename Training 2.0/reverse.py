def reverse(n,rev=0):
    if n==0:
        return rev
    return reverse(n // 10, rev*10 + n%10)

n = int(input("Enter the n value :"))
print("Reverse number : ",reverse(n))