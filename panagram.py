s=input().lower()
r=0
d=[chr(i) for i in range(97,123)]
for i in s:
	if i in d:
		r=r+1
if r==26:
	print("yes")
else:
	print("no")
