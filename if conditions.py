"if statement" means: if so,do this or print this statement.
"elif: statement" means:otherwise do this, if "if statement" was not true.
else:means:if none of conditions was not true,do or print this.
a = 10.5
b = 12.5
c = 8

if a == b:
    print("a and b is equal")
elif a > b:
    print("a is greater than b")
elif c < a and b:
    print("c is smaller than a and b ")
else:
    print("none of conditions is not true")
# output:c is smaller than a and b

NESTED IF:
a = 20
if a <= 20:
    print("a is greater than 10")
    if a < 20:
        print(" a is smaller than 10")
    else:
        print("empty")
# output:a is greater than 10
# empty

point: in the nested if(example above)  if the first statement is not true, conditions
will not work. 
if statement cannot be empty,to avoid getting an error,put in the (pass):
a = 1
b = 2
if a < b:
    pass
