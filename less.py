n=int(input())
l=list(map(int,input().split(" ")))
k=0
for i in l:
	for j in l:
		if i<j:
			k=k+1
print(k)
