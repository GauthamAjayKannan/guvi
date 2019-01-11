#prime
nu=int(input())
count=0
for i in range(2,nu):
	if nu%i==0:
		count=count+1
print("yes" if count==0 else "no")    
