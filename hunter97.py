def gcd(m,n):
	if m<n:
		m,n=n,m
	if m%n==0:
		return n
	else:
		return gcd(n,m%n)
a,b=list(map(int,input().split(" ")))
s=gcd(a,b)
if s==1:
	print("yes")
else:
	print("no")
