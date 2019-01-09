n=int(input())
a,b,nu=0,1,0
l=[]
for i in range(n):
    l.append(b)
    nu=a+b
    a=b
    b=nu  
print(*l)
