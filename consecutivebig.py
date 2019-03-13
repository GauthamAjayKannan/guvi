n=int(input())
l=list(map(int,input().split(" ")))
r=[max([l[i],l[i+1]]) for i in range(n-1)]
print(*r)
