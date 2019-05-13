n=int(input())
l=list(map(int,input().split(" ")))
for i in range(1,n):
	if sum(l[:i])//len(l[:i])==sum(l[i:])//len(l[i:]):
		print("yes")
		break
else:
	print("no")
