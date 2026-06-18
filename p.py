# wap to read name,age,print the char at that position alphabetially when sum of digits in age reaches 1 - 26
age = input("Enter your age: ").strip()
digit_sum = sum(int(ch) for ch in age if ch.isdigit())

if 1 <= digit_sum <= 26:
    letter = chr(ord('a') + digit_sum - 1)
    print(letter)
else:
    print("Sum of digits is not in range 1-26")