n=input()
l=list(map(int,input().split(" ")))
di={l[i]:i for i in range(len(l))}
while len(l)!=1:
	l=[l[i] for i in range(1,len(l),2)]
print(di[l[0]])
