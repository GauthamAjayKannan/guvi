#lessthank
n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
r=[i for i in l if i<k]
print(*sorted(r))
