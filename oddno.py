n,m=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
l=[i for i in l if i%2]
print(l[m-1])
