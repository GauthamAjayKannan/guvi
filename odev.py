n=int(input())
l=list(map(int,input().split(" ")))
n=0
r=[i%2 for i in l]
print(l[r.index(0)] if r.count(0)==1 else l[r.index(1)])
