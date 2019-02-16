s1,s2=input().split(" ")
t=""
while len(s2)!=0:
	t=s2[:2]
	print(t)
	s2=s2[1:]
	if t in s1:
		print("yes")
		break
else:
	print("no")
