#perfectsquare
n,m=list(map(int,input().split()))
i=1
while i<(n*m):
	if i==(n*m)//i:
		print("yes")
		break
	i=i+1
if i==(n*m):
	print("no")
elif (n*m)==0:
	print("yes")
