n=int(input())
l=list(map(int,input().split(" ")))
r=1
res=0
for i in range(len(l)-1):
	if l[i]<l[i+1]:
		r=r+1
	else:
		if res<r:
			res=r
		r=1
if res<r:
	res=r
print(res)
