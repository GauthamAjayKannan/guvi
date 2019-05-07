s=input()
a=0
r=""
count=1
while a<len(s):
	t=""
	if count%2 and s[a].isalpha():
		t=s[a].upper()
		count+=1
	elif s[a].isalpha():
		t=s[a]
		count+=1
	else:
		t=s[a]
	r+=t
	a+=1
print(r)
