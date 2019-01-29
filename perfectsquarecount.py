#perfectsquarecount
l,r=list(map(int,input().split(" ")))
count=0
for i in range(l,r+1):
	v=0
	for j in range(1,i):
		v=j*j
		if v==i:
			count=count+1
			break
		elif v>i:
			break
		else:
			pass
print(count)
