s=input()
v,c="",""
for i in s:
	if i in ["a","e","i","o","u"]:
		v+=i
	else:
		c+=i
print(v+c)
