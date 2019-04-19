n=input()
r=[]
ch=False
for i in n:
	if i in r:
		ch=True
		print("yes")
		break
	else:
		r.append(i)
if not(ch):
	print("no")
