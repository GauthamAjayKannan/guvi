n=int(input())
r=[]
while n!=0:
	r.append(str(n%2))
	n=n//2
print("".join(r[::-1]))
