strings are arrays,then you can return names by using index([:]):
: means up to
first index is 0 but when you want to return a word from the end,the first index is -1
st = "my name is allen"
print(st[2:6])
# output = nam

point: space is counted e.g:
st = "myname is allen"
print(st[2:6])
# output = name
this two prints act the same,the second one is the easiest way and more logical
st = "myname is allen"
print(st[14])
# output:n
print(st[-1])
# output:n

to return a special words:
string1 = 'this is the first class'
print(string1[-5:-2])
# output:cla
point:to solve it,you should subtract (5-2) = 3 then it starts from -5 up to 3 but not included 3
print(string1[-5:-3]) 
# output:cl

to reverse the words,use (::-1),it means from the end up to the first e.g:
st = "my name is allen"
print(st[::-1])
# output:nella si eman ym

python string methods:
(capitalize(),casefold(),center(),count(),encode(),endswith(),expandtabs(),find(),format(),
format_map(),index(),isalnum(),isalpha(),isdecimal(),isdigit(),isidentifier(),islower(),
isnumeric(),isprintable(),isspace(),istitle(),issuper(),join(),ljust(),lower(),partition(),
replace(),rfind(),rindex(),rjust(),rstrip(),rpartition(),rsplit(),split(),splitlines(),
startswith(),strip(),swapcase(),title(),translate(),upper(),zfill())

the most used python string methods examples:
uppercase the first letter:
text = 'this is the first rainy day/snowy day'
print(text.capitalize())
# output:This is the first rainy day/snowy day
to center a string:
text = 'this is the first rainy day/snowy day'
print(text.center(70))
# output:                this is the first rainy day/snowy day
to return the numbers of times a special string appears:
text = 'this is the first rainy day/snowy day'
print(text.count('day'))
#output:2
to encode string:
text = 'this is the first rainy day/snowy day'
print(text.encode())
# output:b'this is the first rainy day/snowy day'
to find a string:
string.find(value,start,end)
text = 'this is the first rainy day/snowy day'
print(text.find("f"))
# output:12
text = 'this car is {} and made by {}'
print(text.format({'BENZ'},{'GERMANY'}))
print(text)
# output: this car is BENZ and made by GERMANY
to join a string:
text = ['amy','allen','tex']
print("".join(text))
#output:amyallentex

point: strings doesnt support item assignment but you can use replace() instead.
st = "my name is allen"
st[1]= 'w'
print(st.replace('y','w',))
to split a string into a list:
text = 'this is the first rainy day/snowy day'
print(text.split())
# output:['this', 'is', 'the', 'first', 'rainy', 'day/snowy', 'day']
strip: to remove spaces
text = ',000000000this is the first rainy day/snowy day,5555'
print(text.strip(",0 5"))
# output:this is the first rainy day/snowy day
to upper all the strings:
text = 'this is the first rainy day/snowy day'
print(text.upper())
# output:text =THIS IS THE FIRST RAINY DAY/SNOWY DAY
point:string doesnt concatenate with integer,to solve this you can use casting