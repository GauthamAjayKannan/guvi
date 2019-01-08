#spacecount
s=input()
count=0
for i in s:
	if i.isspace():
		count=count+1
print(count)
