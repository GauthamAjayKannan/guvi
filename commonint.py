#commonint
n=input()
l1=input().split(" ")
l2=input().split(" ")
r=[]
for i in l1:
	if i in l2 and i not in r:
		r.append(i)
print(*r)
