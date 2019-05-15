n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
for i in range(len(l)):
	l[i]-=k
	if l[i]<0:
		l[i]=0
print(l.count(0))
