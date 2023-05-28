function usages:it helps to have readable codes and seperate the parts of program and
it reduces repetitive codes.
function should be called when it is run.
def myfunction():
    print('hello,this is first function.')
myfunction()
# output:hello,this is first function.

parameters:parameters ARE SPECIFIED AFTER THE FUNCTION NAME,INSIDE THE PARANTHESES.
def myfunction(firstname):
    print(firstname)
myfunction('david')
# output:david
parameters IN THE EXAMPLE ABOVE IS firstname and you should also specify the firstname in calling
funtion or ARGUMENTS('david').

point:function must be called the correct number of argument if not,it will raise an error.
def myfunction(firstname,lastname):
    print(firstname,lastname)
myfunction('david','taylor')
# output:david taylor

*ARGS:if you dont know how many arguments that will be passed into your function,add * before the 
parameter name,if you dont do this,it will raise an error
def myfunction(*students):
    print(students)
myfunction('david','aston','english')
# output:('david', 'aston', 'english')
OR:
def myfunction(*students):
    print(students[1])
myfunction('david','aston','english')
# output:aston

**KWARGS:if you dont know how many keyword arguments that will be passed into your function,
add * before the parameter name,if you dont do this,it will raise an error.
def myfunction(**tree):
    print(tree)
myfunction(color1 = "blue",name1 = "flower",color2= 'green',name2 = "plant")
# output:{'color1': 'blue', 'name1': 'flower', 'color2': 'green', 'name2': 'plant'}
OR:
def myfunction(**tree):
    print(tree["name1"])
myfunction(color1 = "blue",name1 = "flower",color2= 'green',name2 = "plant")
# output:flower

DEFAULT PARAMETER VALUE:
def myfunction(objects = "HOUSE"):
    print(objects)
myfunction()
myfunction("planet")
myfunction("cat")
myfunction("desk")
# output:
# HOUSE
# planet
# cat
# desk

HOW TO PASS A LIST:
def myfunction(fruits):
    for objects in fruits:
        print(objects)
newlst = ["avacado","apple","orange"]
myfunction(newlst)
# output:
# avacado
# apple
# orange

return: returns a value and put it in the place of arguments.
point:use print()before the argument to run the function.
def myfunction(power):
    return 7 **power
print(myfunction(2))
# output:49

def myfunction():
    pass
myfunction()

RECURSION:IT IS A KIND OF LOOPS MEANING THAT IT GOES AND COMES BACK.
def myf(i):
    if i>= 10:
        pass
    else:
        print(i)
        myf(i+1)
        print(i)
myf(1)
# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
