#largestno
n=int(input())
l=input().split(" ")
l.sort(reverse=True)
print("".join(l))
