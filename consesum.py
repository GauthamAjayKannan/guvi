n=int(input())
l=list(map(int,input().split(" ")))
sum=0
for i in range(len(l)-1):
	sum+=l[i]+l[i+1]
print(sum)
