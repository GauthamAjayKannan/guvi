n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
ke=0
for i in range(0,len(l)-1):
	for j in range(i,len(l)):
		if l[i]+l[j]==k:
			print("yes")
			ke=1
			break
	if ke==1:
		break
else:
	print("no")
