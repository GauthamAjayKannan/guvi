n=int(input())
l=list(map(int,input().split(" ")))
res=[]
for i in range(1,len(l)+1):
	res.append(sum(l[:i]))
print(*res)
