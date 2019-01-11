#vowel
s=input()
v=['a','e','i','o','u']
k=0
for i in s:
	if i in v:
	   k=1
	   break
print("yes" if k==1 else "no")
