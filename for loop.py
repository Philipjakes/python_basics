for : iterates over iterating(string,list,tuple,dictionary,set)
unkown = "titanic"
for name in unkown:
    print(name)
# output:
# t
# i
# t
# a
# n
# i
# c

range()function:returns a sequence of numbers,starting from 0 by default.
for number in range(4):
    print(number)
# output:
# 0
# 1
# 2
# 3

for i in range(6):
    print(" ")
    for j in range(6):
        print('j',end = '  ')
in the example above i is column and j is row.
# output:
# j  j  j  j  j  j
# j  j  j  j  j  j
# j  j  j  j  j  j
# j  j  j  j  j  j
# j  j  j  j  j  j
# j  j  j  j  j  j
for x in range(8):
    if x == 5:
        break
    print(x)
else:
    print("end")
# output:
# 0
# 1
# 2
# 3
# 4


# pass:
for x in range(3):
    pass