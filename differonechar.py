#differchar
s1,s2,n=input().split(" ")
n=int(n)
l1,l2,count=list(s1),list(s2),0
for i in range(len(l1)):
	if l1[i]!=l2[i]:
		count=count+1
print("yes" if count==n else "no")
