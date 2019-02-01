#largestno
n=int(input())
l=input().split(" ")
l.sort(reverse=True)
print(int("".join(l)))
