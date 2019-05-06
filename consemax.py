st=input()
a=st[0]
re=1
res=[]
last=""
r=""
ma=0
mae=""
for i in st[1:]:
   if i==a:
        r=i
        re=re+1
        k=True
   else:
        k=False
        last=a
        res.append(a)
        a=i
        res.append(re)
        re=1
if k==True:
    res.append(r)
    res.append(re)
else:
    res.append(a)
    res.append(1)
for i in range(1,len(res),2):
   if ma<res[i]:
       ma=res[i]
       mae=res[i-1]
print(mae,ma)
