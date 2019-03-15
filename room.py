n=int(input())
l=[list(map(int,input().split(" "))) for i in range(2)]
r=1
for i in range(n):
	if l[0][i]==l[1][i]:
		r=r+1
for i in range(n-1):
   for j in range(i,n):
	    if l[1][i]==l[0][j]:
		     r=r+1
print(r)
