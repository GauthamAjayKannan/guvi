n,r=list(map(int,input().split(" ")))
def fact(n):
	r=1
	while n>0:
		r=r*n
		n=n-1
	return r
nf=fact(n)
rf=fact(r)
nmr=fact(abs(n-r))
res=nf//(rf*nmr)
print(res)
