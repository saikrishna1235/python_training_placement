s=input()
s_max=0
for i in range(len(s)):
    temp=''
    count=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            count+=1
            temp+=s[j]
        else:
            if s_max<count:
                s_max=count
                t=temp
            break
print(s_max)
print(t)