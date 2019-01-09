n=int(input())
l=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
for i,j in enumerate(l):
    if i+1==n:
        print(j)
