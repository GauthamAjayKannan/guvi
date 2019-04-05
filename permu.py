def fact(num):
	r=1
	while num>0:
		r=r*num
		num-=1
	return r
n,k=list(map(int,input().split()))
print(fact(n)//fact(n-k))
