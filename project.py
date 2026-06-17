paragraph=input("Enter a paragraph: ")
length=len(paragraph)
print("\n",paragraph[0:50],"....")
print("\n")
if length>=50:
    print("You want to read more")
    value=input("Do you want to read more? (yes/no): ")
    if value.lower()=="yes":
        print(paragraph)
    