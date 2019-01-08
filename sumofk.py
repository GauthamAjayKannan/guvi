si,n=list(map(int,input().split(" ")))
ly=list(map(int,input().split(" ")))
su=0
for i in range(si):
	su=su+ly[i]
	if i+1==n:
		print(su)
		break
	
