n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
r=[]
for i in l:
	if l.count(i)==k and i not in r:
		r.append(i)
print(*r)
