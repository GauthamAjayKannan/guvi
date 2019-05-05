n=input()
n=list(n[::-1])
for i in range(len(n)-1):
	if n[i]==n[i+1]:
		del n[i]
		break
print("".join(n[::-1]))
