#finding vowels in a paragraph
paragraph=" Iam studying in the 2nd year of my graduation."
vowels="aeiou"  
for i in paragraph:
    if i in vowels:
        print(i,end=" ")
