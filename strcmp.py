#strcmp
s1,s2=input().split(" ")
if s1==s2:
	print(s1)
else:
	if len(s1)>=len(s2):
		print(s1)
	else:
		print(s2)
