n=int(input())
l=[]
r=[]
for i in range(2,n+1):
	coun=0
	for j in range(2,i):
		if i%j==0:
			coun=1
	if coun==0:
		l.append(i)
for i in range(len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==n:
		  r.append([l[i],l[j]])
print(*r[0])
