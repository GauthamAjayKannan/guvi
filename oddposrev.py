s=input().split(" ")
r=""
for i in range(len(s)):
	if (i+1)%2:
		r=r+s[i][::-1]
	else:
		r=r+s[i]
	r=r+" "
print(r)
