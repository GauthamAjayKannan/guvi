n,k=input().split(" ")
k=int(k)
r=[]
for i in range(len(n)-k+1):
	r.append(n[i:i+k])
print(*r)
