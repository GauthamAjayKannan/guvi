#armstrong
s,e=input().split(" ")
l=[]
for i in range(int(s)+1,int(e)):
	r=0
	u=[int(i) for i in list(str(i))]
	u=[i**3 for i in u]
	r=sum(u)
	if str(r)==str(i):
		l.append(r)
print(*l)
	
