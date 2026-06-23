# s={'hi',1,2,3,4,0}
# l = list(s)
# l[0],l[-1],l[0]
# print(set(l))                                              



s1 = {1,2,3}
s2 = {2,3,4}
print("Difference",s1.difference(s2))
s1.discard(1)
s1.discard(5)
print(s1)
s1.remove(3)
print(s1)
s1.remove(5)
print(s1)