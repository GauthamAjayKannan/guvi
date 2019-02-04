#kpair
n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
key=0
for i in range(len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==k:
			print("yes")
			key=1
			break
	if key==1:
		break
if key==0:
	print("no")
