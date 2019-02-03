# your code goes here
s1,s2=input().split(" ")
for i in s1:
	if i in s2:
		print("yes")
		break
else:
	print("no")
