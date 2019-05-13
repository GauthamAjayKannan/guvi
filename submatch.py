s=input()
while s==s[::-1]:
	s=s[:len(s)-1]
print(s)
