#perimeterarea
p,a=list(map(int,input().split(" ")))
count=0
for i in range(1,a):
	for j in range(i,a):
		ar=i*j
		if ar==a and 2*(i+j)==p:
			print("yes")
			count=1
			break
		else:
			pass
	if count==1:
		break
else:
	print("no")
