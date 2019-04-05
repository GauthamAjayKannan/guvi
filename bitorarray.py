n=int(input())
l=list(map(int,input().split(" ")))
r=l[0]
if len(l)==1:
	print(r)
else:
	for i in l[1:]:
		r=r|i
	print(r)
