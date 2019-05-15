n=list(input())
r=0
for i in range(len(n)-1):
	t=n.copy()
	if n[i]==n[i+1]:
		t.pop(i)
		if r<int("".join(t)):
			r=int("".join(t))
print(r)
