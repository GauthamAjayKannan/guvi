#powerofn
l,n=list(map(int,input().split(" ")))
i=1
while True:
	if l==n**i:
		print("yes")
		break
	elif i**2>l:
		print("no")
		break
	else:
		i=i+1
