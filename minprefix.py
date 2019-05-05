n=input()
l=input().split(" ")
p=input()
coun=0
for i in l:
	if p==i[:len(p)]:
		coun+=1
print(coun)
