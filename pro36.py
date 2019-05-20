n=input()
l=list(map(int,input().split(" ")))
count=0
for i in range(len(l)-1):
	for j in range(i+1,len(l)):
		for k in range(j+1,len(l)):
			if l[i]>l[j] and l[i]>l[k] and l[j]>l[k]:
				count+=1
print(count)
