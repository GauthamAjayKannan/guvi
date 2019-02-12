n=int(input())
l=list(map(int,input().split(" ")))
r=0
for i in range(len(l)-1):
	for j in range(i+1,len(l)):
	  if l[i]<l[j]:
		   r=r+1
print(r)
