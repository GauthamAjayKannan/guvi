#choco
n=int(input())
k=[[i,1] for i in list(map(int,input().split(" ")))]
k.sort()
for i in range(len(k)-1):
	if k[i+1][0]>k[i][0]:
		while k[i+1][1]<=k[i][1]:
			k[i+1][1]=k[i+1][1]+1
	else:
		k[i+1][1]=k[i][1]
print(k)
