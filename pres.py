n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
while k in l:
	l.remove(k)
print(*l)
