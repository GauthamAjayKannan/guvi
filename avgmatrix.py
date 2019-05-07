n=int(input())
l=[list(map(int,input().split(" "))) for i in range(n)]
s=0
for i in l:
	for j in i:
		s=s+j
print(round(s/n**2,6))
