n=input()
res=0
j=0
for i in n[::-1]:
	res=res+int(i)*2**j
	j+=1
print(res)
