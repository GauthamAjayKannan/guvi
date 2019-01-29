#stringrotate
s,n=input().split(" ")
n,i,s=int(n),1,s
while i<=n:
	u=s[-1:]
	s=u+s[:len(s)-1]
	i=i+1
print(s)
