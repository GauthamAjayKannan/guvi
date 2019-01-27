#klargest
n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
print(sorted(l)[::-1][k-1])
