si,n=list(map(int,input().split(" ")))
ly=list(map(int,input().split(" ")))
for i in range(si):
	sum=sum+ly[i]
	if i+1==n:
		print(n)
		break
	
