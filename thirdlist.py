n=input()
l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
r=[]
for i in range(len(l1)):
	r.append(l1[i]+l2[i])
print(*r)
