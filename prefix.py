#longestprefix
n=int(input())
l=[input() for i in range(n)]
res,key="",0
for i in range(len(min(l,key=len))):
	res=res+l[0][i]
	for j in l[1:]:
		if j.startswith(res):
			pass
		else:
			key=1
			break
	if key==1:
		res=res[:len(res)-1]
		break
print(res)
