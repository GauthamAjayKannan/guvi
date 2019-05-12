n=int(input())
l=[list(map(int,input().split(" "))) for i in range(n)]
d1,d2=1,1
i,j=0,len(l)-1
while i<len(l):
	d1*=l[i][i]
	d2*=l[i][j]
	i+=1
	j-=1
print(d1+d2)
