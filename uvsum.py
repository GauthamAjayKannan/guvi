n1,n2=list(map(int,input().split(" ")))
r=list(map(int,input().split(" ")))
re=[]
ar=[list(map(int,input().split(" "))) for i in range(n2)]
re=[sum(r[i[0]-1:i[1]]) for i in ar]
for i in re:
	print(i)
