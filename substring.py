paragraph="Iam studying in the 2nd year of my graduation."
#first occurance of letter and when it occur again that is 1 substring like check all letters from starting and give the count of substrings ans print the substring using nested for loop
for i in range(len(paragraph)):
    count=0
    for j in range(i+1,len(paragraph)):
        if paragraph[i]==paragraph[j]:
            count+=1
    if count==0:
        print(paragraph[i],end=" ")