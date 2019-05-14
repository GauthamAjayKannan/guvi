#hunter29
x = int(input())
l = list(map(int,input().split()))
y =max(l)
for i in range(x):
	for j in range(x):
		if (i+j)<=x:
			if y<sum(l[j:((i+j))+1]):
				y = sum(l[j:((i+j))+1])
print(y)
