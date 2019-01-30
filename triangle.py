#triangle
a,b,c=list(map(int,input().split(" ")))
print("yes" if a+b+c==180 and a!=0 and b!=0 and c!=0 else "no")
