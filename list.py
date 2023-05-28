list items are ordered,changebale,allow duplicate values and first item has index[0].
list items can be of any data type(string,int,boolean)
newlist = ['jack','patrick','anderson']
print(newlist)
# output:['jack', 'patrick', 'anderson']

newlist = ['jack','patrick','anderson','jack']
print(newlist)
# output:['jack', 'patrick', 'anderson','jack']

len()function: to determine how many items a list has.
newlist = ['jack','patrick','anderson','jack']
print(len(newlist))
# output:4

type():to determine what data type it is:
newlist = ['jack','patrick','anderson','jack']
print(type(newlist))
# output:<class 'list'>

list(()):list constructor uses to make a list.
newlist = list(('jack','patrick','anderson','jack'))
print(newlist)
# output:['jack','patrick','anderson','jack']

ACCESS ITEMS:
newlist = ['jack','patrick','anderson']
print(newlist[-3:-1])
# output:['jack','patrick']

newlist = ['jack','patrick','anderson']
if 'paterson' in newlist:
    print("yes")
else:
    print("no")
# output:no

CHANGE ITEMS:
newlist = ['jack','patrick','anderson']
newlist[2]='paterson'
print(newlist)
# output:['jack','patrick','paterson']

newlist = ['jack','patrick','anderson']
newlist[:2]='paterson','jason'
print(newlist)
# output:['paterson', 'jason', 'anderson']

# insert()method:inserts an item at the specific index:
newlist = ['jack','patrick','anderson']
newlist.insert(1,"cherry")
print(newlist)
# output:['paterson',cherry, 'jason', 'anderson']

newlist = ['paterson', 'jason', 'anderson']
autolist = ['benz','bmw','volvo']
newlist+=autolist
print(newlist)
# output:['paterson', 'jason', 'anderson', 'benz', 'bmw', 'volvo']

append() method TO ADD LIST ITEMS:
newlist = ['paterson', 'jason', 'anderson']
newlist.append('crystal')
print(newlist)
# output:['paterson', 'jason', 'anderson', 'crystal']
the insert()method is also used to add items.

extend() method:to append elements from another list to the current list:
newlist = ['paterson', 'jason', 'anderson']
autolist = ['benz','bmw','volvo']
newlist.extend(autolist)
print(newlist)
# output:['paterson', 'jason', 'anderson', 'benz', 'bmw', 'volvo']

newlist = ['paterson', 'jason', 'anderson']
thistuple =('apple','pineapple')
newlist.extend(thistuple)
print(newlist)
# output:['paterson', 'jason', 'anderson', 'apple','pineapple']

REMOVE LIST ITEMS:
newlist = ['paterson', 'jason', 'anderson']
newlist.remove('jason')
print(newlist)
# output:['paterson', 'anderson']

pop():remove the last item by default and also removes the specified item:
newlist = ['paterson', 'jason', 'anderson']
newlist.pop()
print(newlist)
# output:['paterson', 'jason']

newlist = ['paterson', 'jason', 'anderson']
newlist.pop(0) 
print(newlist)
# output:['jason', 'jason']

del()method: 
newlist = ['paterson', 'jason', 'anderson']
del newlist
print(newlist)
# output:name "newlist" is not defined.
newlist = ['paterson', 'jason', 'anderson']
del newlist[1]
print(newlist)
# output:['paterson', 'anderson']

clear():clears the list
newlist = ['paterson', 'jason', 'anderson']
newlist.clear()
print(newlist)
# output:[]

LOOP THROUGH THE INDEX NUMBERS:
newlist = ["cherry","mango","lemon"]
for fruits in range(len(newlist)):
    print(newlist[fruits])
# output:
# cherry
# mango
# lemon

USING WHILE LOOP:
newlist = ["cherry","mango","lemon"]
i = 0
while i < len(newlist):
    print(newlist[i])
    i+=1
# output:
# cherry
# mango
# lemon

LIST COMPREHENSION:
newlist = ["cherry","mango","lemon","car","coin"]
lst = []
for i in newlist:
    if "c" in i:
        lst.append(i)
print(lst)    
# output:['cherry', 'car', 'coin']

fruits = ["cherry","mango","lemon","car","coin"]
newlist = [x for x in fruits if x != "mango"]
print(newlist)
# output:['cherry','lemon', 'car', 'coin']

SORT LISTS alphanumerically:
fruits = ["cherry","mango","lemon","car","coin"]
fruits.sort()
print(fruits)
# output:['car', 'cherry', 'coin', 'lemon', 'mango']

number = [1,22,4,78,6]
number.sort()
print(number)
# output:[1, 4, 6, 22, 78]

SORT DECENDING:
fruits = ["cherry","mango","lemon","car","coin"]
fruits.sort(reverse=True)
print(fruits)
# output:['mango', 'lemon', 'coin', 'cherry', 'car']

number = [1,22,4,78,6]
number.sort(reverse=True)
print(number)
# output:[78, 22, 6, 4, 1]

CUSTOMIZING SORT FUNCTION:           
cars = [
    ("BMW",1980),
    ("BENZ",2020),
    ("CHEVROLET",1985),
]

def sort_item(item):
    return item[1]
cars.sort(key=sort_item,reverse=True)
print(cars)

COPY A LIST:
number = [1,22,4,78,6]
copy = number.copy()
print(copy)
# output:[1,22,4,78,6]

number = [1,22,4,78,6]
lis = list(number)
print(lis)
# output:[1,22,4,78,6]

JOIN TWO LISTS:
number = [1,22,4,78,6]
names = ["jackson","mickael","lisa"]
for nam in names:
    number.append(nam)
print(number)
# output:[1, 22, 4, 78, 6, 'jackson', 'mickael', 'lisa']
OR:
newlist = number+names
print(newlist)
# output:[1, 22, 4, 78, 6, 'jackson', 'mickael', 'lisa']
OR:
number.extend(names)
print(number)
# output:[1, 22, 4, 78, 6, 'jackson', 'mickael', 'lisa']
