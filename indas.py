#indas
n=int(input())
l=list(input().split(" "))
for i in range(0,len(l)):
	if l[i]<l[i+1]:
		pass
	else:
		print(l.index(l[i]))
		break
