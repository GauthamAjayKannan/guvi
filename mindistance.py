n=input()
l=list(map(int,input().split(" ")))
u,v=list(map(int,input().split(" ")))
s=0
dis=1
for i in range(len(l)):
	if l[i]==u or l[i]==v:
		s=i
		break
for j in range(s,len(l)-1):
	if l[j+1]==u or l[j+1]==v:
		break
	else:
	    dis=dis+1
print(dis)
