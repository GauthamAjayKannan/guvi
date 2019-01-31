# your code goes here
n,m=list(map(int,input().split(" ")))
l=[input().split(" ") for i in range(n)]
r=[]
for i in l[0]:
	count=1
	for j in l[1:]:
		if i in j:
			count=count+1
	if count==n:
		r.append(i)
print(*sorted(r))
		
