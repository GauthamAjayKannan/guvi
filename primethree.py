n=int(input())
pr=[]
l=[]
for i in range(2,n):
	coun=0
	for j in range(2,i):
		if i%j==0:
			coun=1
	if coun!=1:
		pr.append(i)
for i in range(len(pr)):
	for j in range(len(pr)-1):
		if pr[i]+pr[j]+pr[j+1]==n:
			l.append(sorted([pr[i],pr[j],pr[j+1]]))
if len(l)>2:
	min=l[0]
	print(min)
	for i in range(1,len(l)):
		if i[0]<min[0] and i[1]<min[1]:
			min=i
	print(*min)
else:
	print(*l[0])
