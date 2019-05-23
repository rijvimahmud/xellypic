print ("hello world")



if 5>2:

  print("five is greater than two")
  """this is a docstrings"""
  print('hello world')
  print("hello world")
  print("hello")
  print("hello world")
  if 5>2:
      print("five is greater than two")

x=5
y="Cezanne_15"
print(x)
print(y)
x= "awesome"
print("python is " + x)
x="Python is "
y="awesome"
z= x+y
print(z)
x=5
y=10
print(x+y)
print("hello")

x=5
y=10
print(x+y)
print("hello")
if 5 > 3:
    print("five is grater than three")
    if 5>2:
        print("five is grater than two")
        x=1
        y=2.8
        z=3j
        print(type(x))
        print(type(y))
        print(type(z))
        x=(3)
        y=(5j)
        z=x+y
        print(z)
        x=2
        y=5

        print(x+y)
        x= int(2)
        y= int(2.8)
        z= int("3")
        print(x)
        print(y)
        print(z)
        x=float(1)
        y=float(2.8)
        z=float(3)
        w=float(4.3)
        print(x)
        print(y)
        print(z)
        print(w)
        x=str(1)
        y=str(3j)
        z=str(4.0)
        print(x)
        print(y)
        print(z)
a="hello world"
print(a[3])
b="hello world"
print(b[3:8])
#The strip() method removes any whitespace from the beginning or the end:
a="   hello world    "
print(a.strip())
#The len() method returns the length of a string:
a="hello world"
print(len(a))
#The lower() method returns the string in lower case:
a="HELLO WORLD"
print(a.lower())
#The upper() method returns the string in upper case:
a="hello world"
print(a.upper())
#The replace() method replaces a string with another string:
a="hello world"
print(a.replace("h" , "J"))
#The split() method splits the string into substrings if it finds instances of the separator:
a="hello world"
b=a.split()
print(b)

e=2
r=3
t= e + r
print(t)
#Python Arithmetic Operators
x=3
y=6
z=(y/x)
print(int(z))
a=10
b=3
c= a%b
print(c)
a=2
b=3
c= a**b
print(c)
a=9
b=2
c=a//b
print(c)
#Python Assignment Operators
x = 4
x += 3
print(x)
x=4
x-=5
print(x)
x=3
x*=3
print(x)
x=3
x/=3
print (x)
x=5
x%=3
print(x)
x=10
x//=3
print(x)
x=3
x**=3
print (x)
#Python Comparison Operators
x=3
y=4
print (x == y)

x=3
y=4
print ( x != y)

x=4
y=2
print (x > y)

x=3
y=2
print (x < y)

x=3
y=3
print (x >= y)

x=4
y=3
print (x <= y)

#Python Logical Operators
x=4
print (x >3 and x<5)

x=5
print (x >10 or x<10)

x=4
print (not(x > 3 and x<5))

#python lists

#list
thislist = ["apple", "banana", "cherry"]
print (thislist)

#Access Items

thislist = ["apple", "banana", "cherry"]
print (thislist[1])

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1]= "coconut"
print (thislist)

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print (x)

 #Check if Item Exists
 thislist = ["apple", "banana", "cherry"]
 if "apple" in thislist:
     print("yes, 'apple' in this list")

#List Length
     thislist = ["apple", "banana", "cherry"]
     print(len(thislist))

#Add Items
     thislist = ["apple", "banana", "cherry"]
     thislist.append ("orange")
     print (thislist)

#To add an item at the specified index, use the insert() method:
     thislist= ["apple", "banana", "cherry"]
     thislist.insert (1, "orange")
     print (thislist)
#Remove Item
     thislist = ["apple", "banana", "cherry"]
     thislist.remove ("banana")
     print (thislist)

     thislist= ["apple", "banana", "cherry"]
     thislist.pop()
     print (thislist)

     thislist = ["apple", "banana", "cherry"]
     del thislist [1]
     print (thislist)



     thislist = ["apple", "banana", "cherry"]
     thislist.clear()
     print (thislist)

#copy a list

     thislist = ["apple", "banana", "cherry"]
     mylist = thislist.copy()
     print (mylist)


     thislist = ["apple", "banana", "cherry"]
     mylist = list (thislist)
     print (mylist)

#The list() Constructor
thislist = (("apple", "banana", "cherry"))
print (thislist)

#Tuple

thistuple = ("apple", "banana", "cherry")
print (thistuple)

#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print (thistuple[0])

#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.


#Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


#Check if Item Exists

    thistuple = ("apple", "banana", "cherry")
    if "apple" in thistuple:
        print ("yes, 'apple' is in this fruit list")

#Tuple Length

    thistuple = ("apple", "banana", "cherry")
    print (len(thistuple))

#Remove Items
#Note: You cannot remove items in a tuple.

#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
   # thistuple = ("apple", "banana", "cherry")
   # del thistuple
    #print (thistuple)#

#The tuple() Constructor
thistuple= tuple(("apple", "banana", "cherry"))

print(thistuple)

#Set
thisset = {"apple", "banana", "cherry"}
print (thisset)


#Access Items

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print ("banana" in thisset)

#Add Items
#To add one item to a set use the add() method.

#To add more than one item to a set use the update() method.

thisset = {"apple", "banana", "cherry"}
thisset.add ("orange" )
print (thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update (["orange", "mango"])
print (thisset)

#Get the Length of a Set

thisset = {'apple', 'mango', 'cherry', 'banana', 'orange'}
print (len(thisset))

#Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print (thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("cherry")
print (thisset)

thisset = {"apple", "banana", "cherry"}
x= thisset.pop()
print (x)
print (thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The set() Constructor
thisset = set (("apple", "banana", "cherry"))
print (thisset)


#Dictionary

thisdict = {
    "brand" : "porsche",
    "model" : "mustang",
    "year"  : 1964
    }
print (thisdict)

#Accessing Items

thisdict = {
    "brand" : "porsche",
    "model" : "mustang",
    "year" : 1964

    }
x= thisdict["model"]
print (x)

thisdict = {
    "brand" : "porsche",
    "model" : "mustang",
    "year" : 1964

    }
x= thisdict.get("model")
print (x)

#Change Values
thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964



    }
thisdict["year"] = 2018
print (thisdict)

#Loop Through a Dictionary

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
for x in thisdict:
    print (x)


thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
for x in thisdict:
    print (thisdict[x])


thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
for x in thisdict.values():
    print (x)


thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }

for x, y in thisdict.items():
    print (x, y)


#Check if Key Exists

    thisdict = {
        "brand" : "ford",
        "model" : "mustang",
        "year"  : 1964
        }
    if "model" in thisdict:
        print ("yes, 'model' is one of the keys in thisdict")


#Dictionary Length

thisdict = {
    "brand" : "forg",
    "model" : "mustang",
    "year"  : 1964
    }
print (len(thisdict))

#Adding Items

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
thisdict["color"]= "red"
print (thisdict)

#Removing Items

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
thisdict.pop("year")
print (thisdict)


thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
thisdict.popitem()
print (thisdict)

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
del thisdict ["year"]
print (thisdict)

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
thisdict.clear()
print (thisdict)


#Copy a Dictionary
thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
mydict = thisdict.copy()
print (mydict)

thisdict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964
    }
mydict = dict (thisdict)
print (mydict)

#The dict() Constructor

thisdict = dict (brand="ford", model="mustang", year= 1964)
print (thisdict)

#Python Conditions and If statements
a=300
b=50
if a > b:
    print ("a is greater than b")

#Indentation

#a=33
#b=33
#if b>a:
#print ("b is greater than a")

#Elif
a=33
b=33
if b > a :
    print ("b is greater than a ")
elif a==b:
    print ("b and a are equal")

#Else
a=300
b=400

if b < a :
    print("b is less than a ")
elif b==a :
    print ("b and a is equal")
else :
    print ("b is greater than a")


a=344
b=300
if b > a :
    print("b is greater than a")
else :
    print("a is greater than b")

#Short Hand If
a=300
b=200
if a > b : print("a is greater than b")

#Short Hand If ... Else

s=5
t=6
print ("s is greater than t") if s > b else print("t is greater than s")

a=3
b=3
print("A") if a > b else print ("=") if a==b  else print ("B")


#And

a=3
b=4
c=5
d=6
if a<b and c<d :
    print ("both conditions are true")

#Or
a=4
b=3
c=6
d=5
if a < b or c>d:
    print ("at least one of the conditions is true")

#The while Loop

i=1
while (i<6):
    print(i)
    i+=1

#The break Statement
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1


#The continue Statement
i=0
while i<6:
    i+=1
    if i ==3:
        continue
    print(i)

#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Looping Through a String
for x in "banana":
    print(x)

#The break Statement

fruits=["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break

#Exit the loop when x is "banana", but this time the break comes before the print:
fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x== "banana":
        break
    print(x)

#The continue Statement
fruits=["apple", "banana", "cherry", "orange"]
for x in fruits:
    if x=="banana":
        continue
    print(x)

#The range() Function
for x in range(6):
    print(x)

#Using the start parameter:
for x in range (2, 6):
    print (x)

#Increment the sequence with 3 (default is 1):
for x in range (2, 30, 3):
    print(x)

#Else in For Loop
for x in range (6):
    print(x)
else:
    print("finally finished")


#Nested Loops
adj=["red" , "big", "tasty"]
fru=["apple", "banana", "cherry"]
for x in adj:
    for y in fru:
        print(x,y)


#Creating a Function, Calling a Function
def function():
    print("hello python")
function()

#Parameters
def fname(lname):
    print(lname+" hi")
fname("hello")
fname("python")
fname("programming")

#Default Parameter Value

def my_function(country=" redgreen"):
    print("i am from"+country)
my_function(" sweden")
my_function("india")
my_function("bangladesh")
my_function()

##Passing a List as a Parameter
def good(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

good(fruits)


#Return Values
def my_function(x):
    return 3*x
print(my_function(3))
print (my_function(4))

#Recursion
def tri(k):
    if (k>0):
        result = k+tri(k-1)
        print(result)
    else:
        result=0
    return result
print("Recursion")
tri(5)

#Python Lambda
x = lambda a: a+10
print (x(10))

#Lambda functions can take any number of arguments:
x = lambda a,b : a*b
print(x(5, 6))

#A lambda function that sums argument a, b, and c and print the result:
x = lambda a,b,c : a+b+c
print(x(5,6,6))

#Python Arrays
cars = ["ford", "volvo", "bmw"]
print (cars)

#Access the Elements of an Array
cars = ["ford", "volvo" , "bmw"]
x=cars[1]
print (x)

#Modify the value of the first array item:
cars=["ford", "volvo", "ford"]
cars[0]="toyota"
print(cars)

#The Length of an Array
cars=["ford", "volvo", "bmw"]
x=len(cars)
print(x)

#Looping Array Elements
cars=["ford", "volvo", "bmw"]
for x in cars:
    print(x)

#Adding Array Elements
cars = ["ford", "volvo", "bmw"]
cars.append("honda")
print(cars)

#Removing Array Elements
cars = ["ford", "volvo", "bmw"]
cars.pop(1)
print(cars)

#You can also use the remove() method to remove an element from the array.
cars =["ford", "volvo" , "bmw"]
cars.remove("bmw")
print(cars)

#Create a Class
class myclass:
    x=5
print (myclass)

#Create Object
class cla:
    x=5
p1=cla()
print(p1.x)

#The __init__() Function
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1 = person("john", 36)

print(p1.name)
print(p1.age)

#Object Methods
class person(object):
    """docstring for person"""
    def __init__(self, name, age):
        self.name =name
        self.age = age

    def myfunc(self):
        print("hello my name is " + self.name)

p1=person ("john" ,36)
p1.myfunc()

#The self Parameter

class person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name=name
        mysillyobject.age=age

    def myfun(abc):
        print("hello this is " + abc.name)

p1=person("john", 36)
p1.myfun()

#Modify Object Properties
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfu(self):
        print("hello i am " + self.name)
p1=person("john", 36)
p1.age=40
print(p1.age)

'''Delete Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age
print(p1.age)'''

'''Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
print(p1)'''
        

    
