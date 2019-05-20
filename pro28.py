n=int(input())
l=list(map(int,input().split(" ")))
l.sort(reverse=True)
sat=1
print(l)
for i in range(len(l)-1):
	if sum(l[i+1:])<=l[i]:
		sat+=1
print(sat)
