n=int(input())
s=0
for i in range(n+1):
	s=s+str(i).count('2')
print(s)
