s=list(input())
r=[]
for i in s:
	if i not in r:
		r.append(i)
print("".join(r[::-1]))
