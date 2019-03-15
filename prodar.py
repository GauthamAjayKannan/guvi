n=int(input())
l=[int(i) for i in input().split(" ")]
r=[]
for i in range(len(l)):
	pro=1
	for j in range(len(l)):
		if i!=j:
			pro=pro*(l[j])
	r.append(pro)
print(*r)
