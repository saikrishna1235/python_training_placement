n=input("Enter the names").split(",")
vowels=["AEIOUaeiou"]
for i in range(len(n)):
    if n[0][-1] in vowels:
        print("Found")
    else:
        print("Not found")
        