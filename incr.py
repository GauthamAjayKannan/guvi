n=int(input())
l=list(map(int,input().split(" ")))
for i in range(len(l)):
	if l[i]>l[i+1]:
		print(l[i])
		break
