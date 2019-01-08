#charactercount
s=input()
count=0
for i in s:
	if not i.isspace():
		count=count+1
print(count)
