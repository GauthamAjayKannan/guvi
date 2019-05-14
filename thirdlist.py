n=input()
l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
r=[l1[i]+l2[i] for i in range(len(l1))]
print(*r)
