n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
for i in range(k):
	a=l[0]
	l=l[1:]
	l.append(a)
print(*l)
