n=input()
l=list(map(int,input().split(" ")))
sum=0
for i in range(len(l)-1):
	if l[i]<=l[i+1]:
		sum=sum+l[i+1]
	else:
		sum+=l[i]
print(sum)
