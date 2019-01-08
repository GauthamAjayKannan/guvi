#numeric
n=input()
for i in n:
	if i.isdigit() or i==".":
		print("yes")
	else:
		print("no")
		break
