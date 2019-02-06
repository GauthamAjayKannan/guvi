#sumpalindrome
s=list(input())
r=sum([int(i) for i in s ])
if str(r)==str(r)[::-1]:
	print("YES")
else:
	print("NO")
