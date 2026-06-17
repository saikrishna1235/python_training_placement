# A
# B C
# D E F
# G H I J
n=5
ch=65
for i in range(n):
    for j in range(i+1):
        print(chr(ch),end=" ")  
        ch+=1  
    print(" ")