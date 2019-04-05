n=int(input())
l=list(map(int,input().split(" ")))
r=[]
for i in l:
	for j in l:
		r.append(i|j)
print(max(r))
