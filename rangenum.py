n=int(input())
s,e=list(map(int,input().split(" ")))
print("yes" if n in range(s+1,e) else "no")
