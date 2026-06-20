'''
recursion isa special technique to execute the block of code number of times,without using loops.
'''
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))