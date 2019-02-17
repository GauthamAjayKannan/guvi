s=input()
t=""
r=[]
for i in s:
	if i not in t:
		t=t+i
	else:
		if t not in r:
		  r.append(t)
		t=""
print(len(max(r,key=len)))
