lambda is a small function and can only have one expression.
x = lambda val:val +22
print(x(11))
# output:33

def myf(myf):
    return lambda d: d * myf
doble = myf(5)
    
print(doble(8))
# output:40