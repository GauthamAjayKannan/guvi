# your code goes here
#indexmatch
n=input()
l=list(map(int,input().split(" ")))
t=enumerate(l)
l=[i[0] for i in t if i[0]==i[1]]
if l==[]:
	print(-1)
else:
	print(*l)
