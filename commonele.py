n,m=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
r=[]
for i in range(n):
	coun=1
	for j in range(n,len(l)):
		if l[i]==l[j]:
			coun+=1
	if coun>=2 and l[i] not in r:
		r.append(l[i])
print(*r)
