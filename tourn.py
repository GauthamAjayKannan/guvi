n=int(input())
count=0
r=0
def power(num):
	i=3
	while True:
		if num==2**i:
			return True
		elif 2**i>num:
			return False
		else:
			i=i+1
while True:
	n=n+count
	if power(n):
		print(r)
		break
	else:
		count=count+3
		r=r+1
