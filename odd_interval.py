#odd series
s,e=list(map(int,input().split(" ")))
l=[]
for i in range(s+1,e):
	if i%2==1:
		l.append(i)
print(*l)
