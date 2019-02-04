#smallestno
n,k=list(map(int,input().split(" ")))
n=list(str(n))
for i in range(k):
	if i%2==0:
		n=n[1:]
	else:
		n=n[:len(n)-1]
print("".join(n))
