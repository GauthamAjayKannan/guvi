n=int(input())
r=[]
coun=0
t=[]
def isprime(n):
	count=0
	for i in range(2,n):
		if n%i==0:
			count=1
			break
	if count==1:
		return False
	else:
		return True
for i in range(2,n):
	if isprime(i):
		r.append(i)
for i in range(0,len(r)):
	for j in range(0,len(r)):
		if r[i]+r[j]==n and r[i] and r[j] not in t:
			t.append(r[i])
			t.append(r[j])
			coun=coun+1
print(coun)
