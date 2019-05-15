s=list(input())
for i in range(len(s)):
	t=s.copy()
	t.pop(i)
	if "".join(t)=="".join(t[::-1]):
		print("YES")
		break
else:
	print("NO")
