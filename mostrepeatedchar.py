# your code goes here
#mostrepeatedstring
s=list(input())
n={}
n={i:s.count(i) for i in s if i not in n}
i=list(n.keys())[list(n.values()).index(max(list(n.values())))]
print(i)
