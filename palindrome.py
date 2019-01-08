#palindrome
n=int(input())
e=n
n=list(str(n))
r="".join(n[::-1])
if e==int(r):
	print("yes")
else:
	print("no")
