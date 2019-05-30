n,m=list(map(int,input().split(" ")))
l=[list(input()) for i in range(n)]
cost=0
for i in l:
	for j in range(len(i)-1):
		if i[j]=='R' and i[j+1]=='R':
			i[j]='G'
			cost+=5
		elif i[j]=='G' and i[j+1]=='G':
			i[j]='R'
			cost+=3
print(cost)
