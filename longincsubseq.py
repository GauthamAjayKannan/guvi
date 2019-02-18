#inc subsequence
n=int(input())
l=list(map(int,input().split(" ")))
coun=1
k=0
le=0
for i in range(k,len(l)-1):
	if l[i]<=l[i+1]:
		coun=coun+1
	elif l[i]>l[i+1]:
		k=i
		if le<coun:
			le=coun
		coun=1
	else:
		pass
if le<coun:
	le=coun
print(le)
