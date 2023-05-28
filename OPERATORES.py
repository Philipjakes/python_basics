operators in python:(+,-,*,/,%,**,//)
print(2*3)
`# output:6
print(6/3)
# output:2
print(8%2)
% -> remainder
# output:0
print(4**3)
**->power
# output:64
print(12//4)
//-> division
# output:3

MOST USED PYTHON ASSIGNMENT OPERATORES,e.g:
(+=,-=,/=,%=,//=,*=,**=,)
a = 3
b = 4
b += 6
print(b)
c = 4
c//=2
print(c)
point:error raised in (c// = 2) or (print(c//=2))

PYTHON COMPARISON OPERATORES,e.g:
a = 'first'
b = 'second'
print(a == b)
== ->equal
# output:False
a = 'first'
b = 'second'
print(a!=b)
# output:True
a = 3
b = 5
print(a>b)
# output:False
a = 3
b = 5
<= ->smaller or equal with
print(a<=b)

PYTHON LOGICAL OPERATORS:
and :returns true if both statements are True,e.g:
a = 7
print(a<8 and a>4)
# output:True
or :returns true if one of statements are true,e.g: 
a = 7
print(a<8 or a>4)
# output:True
a = 7
print(not a)
# output:False

PYTHON IDENTITY OPERATER:
is -> returns true if both variables are the same object
st = 'snow'
bt = 'rain'
st = bt
print(bt is st)
# output:True
is not -> returns true if both variables are not the same object
st = 'snow'
bt = 'rain'
print(bt is not st)
# output:True

PYTHON MEMBERSHIP OPERATORS:
in ->returns true if a specified value is in the list,tuple ... e.g:
st1 = ["car","auto","machine"]
print("car" in st1)
# output:True
not in ->returns true if a specified value is not in the list,tuple ... e.g:
st1 = ["car","auto","machine"]
print("chip" in st1)
# output:False