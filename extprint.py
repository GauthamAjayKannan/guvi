n,k=input().split(" ")
l=[list(map(int,input().split(" "))) for i in range(2)]
l[0].extend(l[1])
print(*sorted(l[0]))
