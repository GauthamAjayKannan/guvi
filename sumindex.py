#sumindex
n=input()
l=list(map(int,input().split(" ")))
for i in range(1,len(l)):
	if sum(l[:i])==sum(l[i+1:]):
		print("yes")
		break
else:
	print("no")
