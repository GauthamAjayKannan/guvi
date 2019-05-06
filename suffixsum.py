n=input()
l=list(map(int,input().split(" ")))
res=[]
for i in range(len(l)):
	r=0
	for j in range(i,len(l)):
		r+=l[j]
	res.append(r)
print(*res)
