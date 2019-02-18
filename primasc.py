n=int(input())
l=[]
for i in range(2,n):
	coun=0
	for j in range(2,i):
		if i%j==0:
			coun=1
	if coun==0:
		l.append(i)
if l==[]:
	print(0)
else:
	print(*l)
