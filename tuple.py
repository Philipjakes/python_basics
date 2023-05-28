tuple are immutable(unchangable):you can not change or add or remove its values and ordered and allow duplicate.
tuple items are indexed,the first has index[0]and can be of any data type.
tup =("tree","plant","planet","tree")
print(tup)
# output:('tree', 'plant', 'planet', 'tree')

tup =("tree","plant","planet","tree")
print(len(tup))
# output: 4

point:add a comma after creating a tuple with one item:
tup = ("house",)
print(type(tup))
# output:<class 'tuple'>
tup = ("house")
print(type(tup))
# output: <class 'str'>

tuple constructor with double round brackets:
tup =tuple(("tree","plant","planet","tree"))
print(tup)
# output:("tree","plant","planet","tree")

tup =("tree","plant","planet","tree")
print(tup[:3])
# output:("tree","plant","planet")

tup =("tree","plant","planet","tree")
if "fruit" in tup:
    print("YES")
else:
    print("NO")
# output:NO

HOW TO CHANGE TUPLE:
tup =("tree","plant","planet","tree")
y = list(tup)
y[2]="ANIMALS"
x = tuple(y)
print(x)

HOW TO APPEND TUPLE:
tup =("tree","plant","planet","tree")
y = list(tup)
y.append("iron")
x = tuple(y)
print(x)
# output:("tree","plant","planet","iron")

HOW TO ADD TUPLE TO A TUPLE:
tup =("tree","plant","planet","tree")
newtuple = ("coffe",)
tup+=newtuple
print(tup)
# output:("tree","plant","planet","coffe")

HOW TO REMOVE A TUPLE:
tup =("tree","plant","planet","tree")
y = list(tup)
y.remove("tree")
newtup = tuple(y)
print(newtup)
# output:(,"plant","planet","tree")
OR:
tup =("tree","plant","planet","tree")
del tup
print(tup)
# output:this will raise an error.

UNPACKING A TUPLE:
tup =("tree","plant","planet","tree")
(black,white,green,red)=tup
print(black)
print(white)
print(green)
print(red)
# output:
# tree
# plant
# planet
# tree

USING ASTERICK:
tup =("tree","plant","planet","tree")
(black,*white,red)=tup
print(black)
print(white)
print(red)
# output:
# tree
# ['plant', 'planet']
# tree

tup =("tree","plant","planet","tree")
for i in range(len(tup)):
    print(tup[i])
# output:
# ree
# plant
# planet
# tree
you can also use "while" loop.

HOW TO JOIN TWO TUPLES:
tup =("tree","plant","planet","tree")
newtup = (10,66,1000)
tup+=newtup
print(tup)
# output:('tree', 'plant', 'planet', 'tree', 10, 66, 1000)

MULTIPLY TUPLES:
tup =("tree","plant","planet")
newtup = tup * 2
print(newtup)
# output:('tree', 'plant', 'planet')

TUPLE METHODS:
count:returns the number of times a specified value appears in tuple.
tup =("tree","plant","planet","tree")
print(tup.count("tree"))
# output:2
index:returns the position of where value is found and raise an error if the value is not found.
tup =("tree","plant","planet","tree")
print(tup.index("planet"))
# output:2
