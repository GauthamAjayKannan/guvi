s=input()
n=0
r=""
while n<len(s):
	if s[n].isalpha():
		r+=s[n]
		n+=1
	else:
		r+=s[n]
		n+=1
		while s[n]==" ":
			n+=1
print(r)
