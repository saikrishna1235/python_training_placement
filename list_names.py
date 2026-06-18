names=input("Enter names").split(",")
vow="aeiouAEIOU"
for name in names:
    vc=""
    cc=""
    for ch in name:
        if ch in vow:
            vc+=ch
        else:
            cc+=ch
    print(name)
    print("Vowels :",vc,"Consonants :",cc)