#doublestring
s=list(input())
if len(s)%2==0:
	c=(len(s)//2)-1
	del s[c]
else:
	c=len(s)//2
	del s[c]
if s[:c]==s[c:]:
	print("YES")
else:
	print("NO")
