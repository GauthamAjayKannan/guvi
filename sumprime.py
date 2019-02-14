l,r=list(map(int,input().split(" ")))
re=0
def isprime(n):
	coun=0
	for i in range(2,n):
		if n%i==0:
			coun=1
			break
	if coun==1:
		return False
	else:
		return True
for i in range(l,r):
	s=sum([int(i) for i in list(str(i))])
	if isprime(s) and s!=1:
		re=re+1
print(re)
