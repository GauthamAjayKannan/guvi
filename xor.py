n=int(input())
a=list(map(int,input().split(" ")))
res=a[0]
for i in a[1:]:
	res=res^i
print(res)
