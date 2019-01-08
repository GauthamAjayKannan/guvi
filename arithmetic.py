#arpg
n,a,d=list(map(int,input().split(" ")))
su=a
t=0
for i in range(2,n+1):
	t=a+(i-1)*d
	su=su+t
print(su)
	
