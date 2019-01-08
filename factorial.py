#factorial
n=int(input())
f=1
if n==1 or n==0:
	print(1)
else:
	while n!=0:
		f=f*n
		n=n-1
	print(f)
