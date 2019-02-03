n=int(input())
l=list(map(int,input().split(" ")))
r=[i for i in l if i<n]
print(*r)
