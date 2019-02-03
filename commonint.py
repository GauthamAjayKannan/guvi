# your code goes here
n=input()
l1=input().split(" ")
l2=input().split(" ")
r=[i for i in l1 if i in l2]
print(*r)
