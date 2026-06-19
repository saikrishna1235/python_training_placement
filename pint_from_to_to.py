#wap to read a number from user and sum the number of digits till it reaches the1 digit then print the character of that position a - k
num = int(input("Enter a number: "))

# Sum digits repeatedly until a single digit is obtained
while num >= 10:
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    num = s

# Convert digit to corresponding character (1->a, 2->b, ...)
ch = chr(ord('a') + num - 1)

print("Single digit:", num)
print("Character:", ch)