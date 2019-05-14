n=input()
l=list(map(int,input().split(" ")))
r=[]
while len(l)!=1:
	r.append(sum(l))
	l=l[:len(l)-1]
r.append(l[0])
print(max(r))
