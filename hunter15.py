n=int(input())
l=list(map(int,input().split(" ")))
ss=max(l)
s=[]
for i in range(len(l)-1):
	ch=True
	for j in range(i+1,len(l)):
		if l[j]>l[i]:
			ch=False
			break
	if ch==True:
		s.append(l[i])
s.append(l[len(l)-1])
print(*s)
print(ss)
