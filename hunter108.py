n=input()
s=0
if len(n)==1:
	s+=int(n)**2
	print(s)
else:
	for i in range(len(n)-1):
		s+=int(n[i])**int(n[i+1])
	s+=int(n[len(n)-1])**int(n[0])
	print(s)
