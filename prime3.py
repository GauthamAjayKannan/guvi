n=int(input())
r,count=[],0
for i in range(3,n+1):
	for j in range(2,i):
		if i%j==0:
			count=1
	if count==0 and str(i).endswith('3'):
		r.append(i)
	count=0
print(sum(r))
