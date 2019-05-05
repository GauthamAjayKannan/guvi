s1=input()
s2=input()
k=False
for i in range(len(s1)):
	a=i
	l=0
	for j in range(len(s2)):
		if  a<len(s1) and s1[a]==s2[j]:
			l=l+1
			a=a+1
		else:
			break
	if len(s2)==l:
		print(i)
		k=True
		break
if k==False:
	print(-1)
