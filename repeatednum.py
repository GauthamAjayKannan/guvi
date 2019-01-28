#repeatednum
n=input()
l=input().split(" ")
d={}
d={i:l.count(i) for i in l if i not in d}
l1=[i for i in d if d[i]>=2]
print(*sorted(l1))
