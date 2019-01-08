#armstrong_number
n=input()
l=[int(i) for i in list(n)]
l=[i**3 for i in l]
r=sum(l)
if n==str(r):
	print("yes")
else:
	print("no")
