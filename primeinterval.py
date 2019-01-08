#prime interval
s,e=list(map(int,input().split(" ")))
l=[]
for i in range(s+1,e):
	count=0
	for j in range(2,i):
		if i%j==0:
			count=count+1
	if count==0:
		l.append(i)
print(*l)
