def prod(l):
	r=1
	for i in l:
		r=r*i
	return r
n=input()
l=list(map(int,input().split(" ")))
r=[]
while len(l)!=1:
	r.append(prod(l))
	l=l[:len(l)-1]
print(max(r))
