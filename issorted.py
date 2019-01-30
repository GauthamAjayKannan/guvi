#issorted
n=input()
l=list(map(int,input().split(" ")))
print("yes" if all(l[i]<=l[i+1] for i in range(len(l)-1)) else "no")
