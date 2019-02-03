#sameline
line=[input().split(" ") for i in range(3)]
print("yes" if line[0][0]==line[1][0]==line[2][0] or line[0][1]==line[1][1]==line[2][1] else "no")
