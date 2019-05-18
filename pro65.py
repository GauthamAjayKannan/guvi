n,k=list(map(int,input().split()))
l=list(map(int,input().split(" ")))
t=int(input())
sum=0
for i in l:
	if l.index(i)!=k:
		sum+=i
sum=round(sum/2)
if abs(sum-t)==0:
	print("Bon Appetit")
else:
	print(abs(sum-t))
