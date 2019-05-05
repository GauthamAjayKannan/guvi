n=input()
l=list(map(int,input().split(" ")))
print(l.index(min(l))+1,l.index(max(l))+1)
