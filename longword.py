s=input().split(" ")
r=s[0]
for i in s[1:]:
	if len(i)>len(r):
		r=i
print(r)
