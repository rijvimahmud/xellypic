print(
    "hello world"
)
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
