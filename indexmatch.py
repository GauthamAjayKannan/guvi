#indexmatch
n=input()
l=list(map(int,input().split(" ")))
t=enumerate(l)
l=[i[0] for i in t if i[0]==i[1]]
print(*l if l!=[] else "-1")
