#str
s=input()
a,b=0,0
for i in s:
	if i.isalpha():
		a=1
	elif i.isnumeric():
		b=1
	else:
		pass
print("Yes" if a==1 and b==1 else "No")
	
