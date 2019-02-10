n=int(input())
l=list(map(int,input().split(" ")))
d={}
d={i:l.count(i) for i in l if i not in d}
print(list(d.keys())[list(d.values()).index(max(d.values()))])
