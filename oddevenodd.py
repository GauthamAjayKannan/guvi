#oddevenevenodd
n=input()
l=list(map(int,input().split(" ")))
u=[]
for i in range(0,len(l)):
	if l[i]%2==0 and i%2:
		u.append(l[i])
	elif l[i]%2 and i%2==0:
		u.append(l[i])
	else:
		pass
print(*u)
