#62
s=input()
b,n=0,0
for i in s:
	if i=="0" or i=="1":
		b=1
	else:
		n=1
		break
print("no" if n==1 else "yes")
