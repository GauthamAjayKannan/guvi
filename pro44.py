n,p,q,r=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
res=0
for i in range(len(l)):
	for j in range(i,len(l)):
		for k in range(j,len(l)):
			  t=p*l[i]+q*l[j]+r*l[k]
			  if t>res:
				   res=t
print(res)
