n,k,t=list(map(int,input().split(" ")))
l=list(map(int,input().split(" ")))
coun=0
for i in range(len(l)-1):
	for j in range(i+1,len(l)):
		if l[i]+l[j]==t:
			print("yes")
			coun=1
			break
	if coun==1:
		break
		
if coun==0:
	print("no")
