n=input()
l=list(map(int,input().split(" ")))
small=l[0]
r=[l[0]]
for i in l[1:]:
	if i<=small:
		small=i
	r.append(small)
print(*r)
