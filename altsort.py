n=int(input())
l=list(map(int,input().split()))
mi=sorted(l)
ma=sorted(l)[::-1]
r=[]
for i in range(n):
	if i%2:
		r.append(mi[0])
		mi=mi[1:]
	else:
		r.append(ma[0])
		ma=ma[1:]
print(*r)
