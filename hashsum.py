def calc(a):
   u=a[:a.index("#")]
   s=0
   r=""
   for i in a:
        if i.isnumeric():
            r=r+i
        elif r!="":
            s=s+int(r)
            r=""
   if r.isnumeric():
      s=s+int(r)
   return u,s
s1=input()
s2=input()
a=calc(s1)
b=calc(s2)
if a[1]>b[1]:
	print(a[0])
else:
	print(b[0])
