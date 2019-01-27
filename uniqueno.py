# your code goes here
l=list(map(int,input().split(" ")))
n={}
n={i:l.count(i) for i in l if i not in n}
print(list(n.keys())[list(n.values()).index(min(list(n.values())))])
