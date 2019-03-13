n=int(input())
l=list(map(int,input().split(" ")))
r=1
for i in range(len(l)):
	if l[i]<l[i+1]:
		r=r+1
	else:
		print(r)
		break
