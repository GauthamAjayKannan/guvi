#specificvalue
n,k=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
count=0
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==k:
			count=1
			print("YES")
			break
	if count==1:
		break
if count==0:
	print("NO")
