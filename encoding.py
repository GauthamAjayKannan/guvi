s1=input()
s2=input()
r=""
a={}
j=1
for i in range(97,123):
	a[chr(i)]=j
	j+=1
for i in range(len(s1)):
	t=a[s1[i]]+a[s2[i]]
	if t>26:
		t-=26
	for k,v in a.items():
		if t==v:
			r+=k
print(r)
