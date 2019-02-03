#kthsmallest
n,k=input().split(" ")
l=input().split(" ")
l.sort()
print(l[int(k)-1])
