def du(num):
	return num if num%2 else du(num//2)
n=int(input())
print(du(n))
