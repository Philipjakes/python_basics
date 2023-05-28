sets are unchangable,unindexed and do not allow duplicate values.
point:set items can appear in a different order every time you use them.
set items can be of any data type.
sett = {"flower","leaf","root","flower"}
print(sett)
# output:{'leaf', 'flower', 'root'}

sett = {"flower","leaf","root","flower"}
print(len(sett))
# output:4

SET CONSTRUCTOR WITH DOUBLE ROUND BRACKETS:
newset = set(("flower","leaf","root"))
print(newset)
# output:{'leaf', 'root', 'flower'}

ACESS ITEMS:IT IS NOT POSSIBLE BUT YOU CAN USE FOR LOOP AND in KEYWORD:
sett = {"flower","leaf","root"}
for newset in sett:
    print(newset)
# output:{'leaf', 'root', 'flower'}

print("sun " in sett)
# output:False
ADD ITEMS:
sett = {"flower","leaf","root"}
sett.add("orange")
print(sett)
# output:{'orange', 'flower', 'leaf', 'root'}

update():to add items from another set:
sett = {"flower","leaf","root"}
newset = {12,34,True}
sett.update(newset)
print(sett)
# output:{'leaf', True, 34, 'root', 'flower', 12}

sett = {"flower","leaf","root"}
newlist = [12,34,True]
sett.update(newlist)
print(sett)
# output:{True, 34, 'leaf', 12, 'root', 'flower'}

HOW TO REMOVE A SET:
if the item to remove does not exist,remove() will raise an error.
sett = {"flower","leaf","root"}
sett.remove("leaf")
print(sett)
# output:{'flower', 'root'}

if the item to remove does not exist,remove() will NOT raise an error.
sett = {"flower","leaf","root"}
sett.discard("leaf")
print(sett)
# output:{'root', 'flower'}

sett = {"flower","leaf","root"}
x = sett.pop()
print(x)                
# output:leaf
removed item
print(sett)
# output:{'flower', 'root'}
the set after removal

sett = {"flower","leaf","root"}
sett.clear()
print(sett)                
# output:set()

sett = {"flower","leaf","root"}
del sett
print(sett)                
# output:this will raise an error.

YOU CAN ONLY USE A SIMPLE FOR LOOP:
sett = {"flower","leaf","root"}
for newset in sett:
    print(newset)
# output:
# flower
# root
# leaf

HOW TO JOIN SETS:
sett = {"flower","leaf","root"}
newset = {12,10,True,"nine"}
Union = sett.union(newset)
print(Union)
# output:{True, 'leaf', 'nine', 10, 'root', 12, 'flower'}
update() is also join the sets.

intersection update():will keep the items that are present in both sets.
sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
sett.intersection_update(newset)
print(sett)
# output:{'flower', 'root'}

intersection():it acts like example above but it will return a new set:
sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
sett.intersection(newset)
print(sett)
# output:{'flower', 'root','leaf'}

symmetric_difference_update(): keep all,but not duplicate.
sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
sett.symmetric_difference_update(newset)
print(sett)
# output:{'club', 'leaf'}

symmetric_difference():will return a new set that contains the elements that are not present 
in both sets.

sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
z = newset.symmetric_difference(sett)
print(z)
# output:{'club', 'leaf'}

set additional methods:
sett = {"flower","leaf","root"}
x = sett.copy()
print(x)
# output:{"flower","leaf","root"}

sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
differ = sett.difference(newset)
print(differ)
# output:{'leaf'}

sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
differ = sett.intersection(newset)
print(differ)
# output:{'flower', 'root'}

isdisjoint():returns true if no items in sett is present in newset.
sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
differ = sett.isdisjoint(newset)
print(differ)
# output:False

issubset():returns true if all items in sett are present in newset.
sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
differ = sett.issubset(newset)
print(differ)
# output:False

issuperset():returns true if all items in sett are present in newset.
sett = {"flower","leaf","root"}
newset = {"flower","club","root"}
differ = sett.issuperset(newset)
print(differ)
# output:False
