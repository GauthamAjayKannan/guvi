#mergeandsort
n=int(input())
r=[]
for i in range(n):
	a=list(map(int,input().split(" ")))
	r.extend(a)
print(*sorted(r))
