n=int(input())
l=list(map(int,input().split(" ")))
r=[]
for i in l:
	for j in l:
		t=abs(i-j)
		r.append(t)
print(max(r))
