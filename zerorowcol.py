#zerorowcolumn
n,m=list(map(int,input().split(" ")))
l=[input().split(" ") for i in range(n)]
r=[]
re=[]
for i in l:
	x=[int(h) for h in i]
	r.append(x)
for i in r:
	re.append(i.copy())
for i in re:
	if 0 in i:
		s=r.index(i)
		y=i.index(0)
		for j in range(n):
			r[j][y]=0
		r[s]=[0]*m
for i in r:
	print(*i)
