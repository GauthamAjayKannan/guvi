s=input()
l=list("dhoni")
r={}
for i in s:
	if i in l and i in r:
		r[i]=r[i]+1
	elif i in l:
		r[i]=1
	else:
		pass
if any(i>1 for i in r.values()) or sum(r.values())!=5:
	print("no")
else:
	print("yes")
