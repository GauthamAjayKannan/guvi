n=int(input())
l=list(map(int,input().split(" ")))
r=[]
for i in range(len(l)):
	for j in range(len(l)):
		if i!=j and abs(l[i]-l[j])!=0:
			r.append(abs(l[i]-l[j]))
print(min(r))
