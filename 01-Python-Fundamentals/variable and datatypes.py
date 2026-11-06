#VARIABLE AND DATA TYPES

#variable is the name of memory loaction where data is stored

#DATA TYPES IN PYTHON

"""
Data   type  	Meaning	       Example
int	   Whole      numbers	           25
float  Decimal    numbers	     25.5
str	   Text	       "Atul"
bool   True or False	         True
list	Collection of values	 [10, 20, 30]
tuple	Ordered, unchangeable collection	(10, 20)
set	    Unique     values	{10, 20, 30}
dict	Key-value  pairs	{"name": "Atul"}

"""

name="Atul Demond"

print("My name is =>> ",name)

a = 24
b = 45

print("sum of a + b =>> ",a+b)

name="Atul Demond"
age=24
height = 6.2
isMale = True


"""
1. Strings (str)
A string is a collection of characters used to store text.

Strings are written inside single quotes (' '), double quotes (" "), or triple quotes.

"""

name = "Atul"
language = 'Python'
message = """Welcome to Python programming"""

print(name)
print(language)
print(message)

language = "PYTHON"

print(language[0])   # P
print(language[1])   # Y
print(language[-1])  # N

name = "  atul demonD  "

print(name.upper())       # ATUL DEMOND
print(name.lower())       # atul demond
print(name.title())       # Atul Demond
print(name.strip())       # Remove extra spaces
print(name.replace("atul", "Rahul"))
print(name.find("demonD"))
print(name.split())       # Convert into list




#list : how to create list 

"""
1. List — []
Mutable (Changeable)
 Ordered


A list is used to store multiple values in a single variable.
- Allows duplicate values.
- Maintains insertion order.
- You can add, remove, and update elements.
- Uses square brackets [].
"""

cars = ["BMW", "MERCEDEZE" , "TOYOTA" , "SUZUKI"]

print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])

cars.append("RANGE ROVER")  #adding element
cars.remove("TOYOTA")       #removing element
cars[0]= "HONDA"            #updating element
cars.pop()                  #removing from last    

print(cars)


#tuple 


"""
2. Tuple — ()
Immutable (Unchangeable)
 Ordered


A tuple is similar to a list, but once you create it, you cannot change its elements.
- Allows duplicate values.
- Maintains insertion order.
- Cannot add, remove, or update elements.
- Uses parentheses ().
"""

cars=("BMW", "ROLLS ROYCE" , "BUGATI" , "HONDA")

print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])

print(cars)


"""
3. Set — {}
Mutable
 Unordered


A set is used to store unique values.
- Does not allow duplicate elements.
- Does not maintain a guaranteed positional order.
- You cannot access elements using indexes.
- You can add and remove elements.
- Uses curly brackets {}.

Method	Purpose
add()	Add an element
remove()	Remove an element
discard()	Remove without error if absent
union()	Combine sets
intersection()	Find common elements
difference()	Find elements only in first set
"""

cars={"BMW", "HONDA", "BUGATI", "LOMABORGHINI"}
cars2={"MG","MARUTIZUKUJKI"}
finalCars = cars.union(cars2)

cars.add("TOYOTA")
cars.remove("HONDA")

print(cars)
print(finalCars)


"""

4. Dictionary — dict
Mutable
 Key-Value Pairs


A dictionary stores data in key-value pairs.

Think of it like a real-world dictionary:
- Word → Meaning
- Key → Value
- Stores data as key-value pairs.
- Keys must be unique.
- Values can be duplicated.
- Maintains insertion order.
- Uses curly brackets {}.
"""

cars = {
    "brand":"Honda",
    "model":"civic",
    "price":40000

}
print(cars)
print("Brand",cars["brand"])

print("model",cars["model"])


student = {
    "name": "Atul",
    "age": 24
}

# Add
student["city"] = "India"

# Update
student["age"] = 25

# Delete
del student["city"]

print(student)


#comprehension:  