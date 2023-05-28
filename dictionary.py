dictionary store date value in key:value pairs,which is ordered,changable and does not allow
duplicate values.
the values in dictionary items can be of any data type(string,boolean,list)
point:dictionaries work with key value.
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999
}
print(diction)
# output:{'john': 'hamson', 'job': 'student', 'years': 1999}

diction = {
    "john":"hamson",
    "job":"student",
    "years":1999
}
print(diction["years"])
# output:1999

diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
print(diction["years"])
# output:2005

diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
print(len(diction))
# output:3

diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
print(type(diction))
# output:<class 'dict'>

HOW TO ACCESS ITEMS:
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
print(diction["job"])
# output:student
OR:
print(diction.get("john"))
# output:hamson

HOW TO GET KEYS:
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
print(diction.keys())
# output:dict_keys(['john', 'job', 'years'])

HOW TO GET VALUES:
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
print(diction.values())
# output:dict_values(['hamson', 'student', 2005])

HOW TO GET ITEMS:
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
print(diction.items())
# output:dict_items([('john', 'hamson'), ('job', 'student'), ('years', 2005)])

diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
if "john" in diction:
    print("YES")
else:
    print("NO")
# output:YES

CHANGE VALUES:
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
diction["john"]="amberson"
print(diction)
# output:{'john': 'amberson', 'job': 'student', 'years': 2005}
OR:
diction.update({"years":1900})
print(diction)
# output:{'john': 'amberson', 'job': 'student', 'years': 1900}

HOW TO ADD ITEMS:
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999,
    "years":2005
}
diction["color"]="white"
print(diction)
# output:{'john': 'hamson', 'job': 'student', 'years': 2005, 'color': 'white'}
OR:
diction.update({"color":"black"})
print(diction)
# output:{'john': 'hamson', 'job': 'student', 'years': 2005, 'color': 'black'}

HOW TO REMOVE ITEMS:
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999
}
diction.pop("years")
print(diction)
# output:{'john': 'hamson', 'job': 'student'}
OR:
diction.popitem()
print(diction)
popitem():removes the last inserted item.
# output:{'john': 'hamson', 'job': 'student'}
OR:
del diction["john"]
print(diction)
# output:{'job': 'student','years':'1999'}
OR:
del diction
print(diction)
# output:it will raise an error
OR:
diction.clear()
print(diction)
# output:{}

looping dictionary:(by referring to the key value)
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999
}
for new_dict in diction:
    print(diction[new_dict])
# output:
# hamson
# student
# 1999

diction = {
    "john":"hamson",
    "job":"student",
    "years":1999
}
for new in diction.values():
    print(new)
# output:
# hamson
# student
# 1999

diction = {
    "john":"hamson",
    "job":"student",
    "years":1999
}
for new in diction.keys():
    print(new)
# output:
# john
# job
# years

diction = {
    "john":"hamson",
    "job":"student",
    "years":1999
}
for key,value in diction.items():
    print(f'the key in diction is:{key} and the values is:{value} ')
# output:
# the key in diction is:john and the values is:hamson 
# the key in diction is:job and the values is:student
# the key in diction is:years and the values is:1999

COPY DICTIONARIES:
diction = {
    "john":"hamson",
    "job":"student",
    "years":1999
}
print(diction.copy())
# output:{'john': 'hamson', 'job': 'student', 'years': 1999}
OR:
print(dict(diction))
# output:{'john': 'hamson', 'job': 'student', 'years': 1999}

NESTED DICTIONARIES:
cars = {
    "car1":{
        "name":"moustang",
        "model":1998
    },
    "car2":{
        "name":"alfa romeo",
        "model":2008
    }
}
print(cars["car2"])
# output:{'car1': {'name': 'moustang', 'model': 1998}, 'car2': {'name': 'alfa romeo', 'model': 2008}}
TO ACCESS THE NAME OF CAR2:
print(cars["car2"]["name"])
# output:alfa romeo

car1={"name":"moustang",
      "model":"1998"
},
car2 = {"name":"moustang",
      "model":"1998"
}
cars = {
    "car1":car1,
    "car2":car2
}
print(cars)
# output:{'car1': {'name': 'moustang', 'model': 1998}, 'car2': {'name': 'alfa romeo', 'model': 2008}}

fromkeys():returns a dictionary with the specified key and value:
key = ('jack','blake','peterson')
value = 50
print(dict.fromkeys(key,value))
# output:{'jack': 50, 'blake': 50, 'peterson': 50}