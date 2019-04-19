n,k=input().split(" ")
ch=True
for i in range(int(k)+1):
	if str(i) not in n:
		ch=False
		print("no")
		break
if ch:
	print("yes")
