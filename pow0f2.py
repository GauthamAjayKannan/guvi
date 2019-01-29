#powof2
n=int(input())
for i in range(0,n):
	if 2**i==n:
		print("yes")
		break
else:
	print("no")
