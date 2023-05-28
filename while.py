while loop:loops as long as a condition is true:
print i as long as i is less than 7:

i = 1
while i < 7:
    print(i)
    i+=1
# output:
# 1
# 2
# 3
# 4
# 5
# 6
point: in the while loop,we have start point(i =1) and end point(i+=1)

i = 1
while i < 7:
    i+=1
    print(i)
# output:
# 2
# 3
# 4
# 5
# 6
# 7

break statement:stop the loop:
i = 1
while i < 7:
    print(i)
    if i == 4:
        break
    i+=1
# output:
# 1
# 2
# 3
# 4


i = 1
while i < 7:
    i+=1
    print(i)
else:
    print("the end of while loop")
# output:
# 2
# 3
# 4
# 5
# 6
# 7
# the end of while loop