n=input()
l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
coun=0
while l1!=l2:
	a=l1[0]
	l1=l1[1:]
	l1.append(a)
	coun+=1
print(coun)
