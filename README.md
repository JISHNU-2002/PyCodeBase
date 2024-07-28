# Python Overview
- High-level, general-purpose language
- Free and runs on any OS
- Interpreted language (not compiled)
- Uses indentation for scope definition (e.g., loops, functions)


### Basic Coding 
```python
# This is a comment
name = "Alice"  # string , assignment
print(name)

age = 25                 # int
height = 5.9             # float
complex_number = 3 + 4j  # complex

result = age + height    # expression
print(result)            # Output: 30.9
print(type(result))      # Output: <class 'float'> : type-conversion

# selection structure(if-else)
if age > 18:
    print("Adult")
else:
    print("Minor")
    
# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# input 
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

### Character Sets
- ASCII stands for American Standard Code for Information Interchange
- ASCII set encoded each keyboard character and several control characters using the integers from 0 through 127
- Python’s `ord() & chr()` functions convert characters to their numeric ASCII codes and back again, respectively
---


# 01 Strings
- immutable data structure
#### capitalize()
- Converts the first character of the string to uppercase
```python
text = "hello world"
print(text.capitalize())  # Output: "Hello world"
```
#### title()
- Converts the first character of each word to uppercase
```python
text = "hello world"
print(text.title())  # Output: "Hello World"
```
#### lower()
```python
text = "Hello World"
print(text.lower())  # Output: "hello world"
```
#### upper()
```python
text = "Hello World"
print(text.upper())  # Output: "HELLO WORLD"
```
#### swapcase()
- Swaps the case of all characters in the string
```python
text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"
```
#### strip()
- Removes leading and trailing whitespace
```python
text = "   Hello World   "
print(text.strip())  # Output: "Hello World"
```
- lstrip
- rstrip
#### replace()
- Adds an element to the end of the list
```python
text = "Hello World"
print(text.replace("World", "Universe"))  
# Output: "Hello Universe"
```
#### split()
- Splits the string into a list of substrings based on a delimiter (default is whitespace)
```python
text = "Hello World"
print(text.split())  # Output: ["Hello", "World"]
```
#### join()
- Joins a list of strings into a single string with a specified delimiter
```python
words = ["Hello", "World"]
print(" ".join(words))  # Output: "Hello World"
```
#### find()
- Returns the lowest index of the substring if found, otherwise -1
```python
text = "Hello World"
print(text.find("World"))  # Output: 6
print(text.find("Universe"))  # Output: -1
```
#### index()
- Returns the lowest index of the substring if found, otherwise raises a ValueError
```python
text = "Hello World"
print(text.index("World"))  # Output: 6
# print(text.index("Universe"))  # Raises ValueError
```
#### count()
```python
text = "Hello World"
print(text.count("l"))  # Output: 3
```
#### startswith() & endswith()
- Returns `True` if the string starts/ ends with the specified prefix, otherwise `False`
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```
#### isdigit() & isalpha() & isalnum() & islower() & isupper()
- Returns `True` if the string follows the condition, otherwise `False`
- isspace()
#### format()
- Formats specified values in a string
```python
text = "Hello, {}. Welcome to {}!"
formatted_text = text.format("Alice", "Wonderland")
print(formatted_text)  
# Output: "Hello, Alice. Welcome to Wonderland!"
```
#### zfill()
- Pads a numeric string with zeros on the left, to fill the specified width
```python
text = "42"
padded_text = text.zfill(5)
print(padded_text)  # Output: "00042"
```
---


# 02 List
#### append()
- Adds an element to the end of the list
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```
#### extend()
- Extends the list by appending all the elements from the iterable
```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
```
#### insert()
- Inserts an element at a specified position
```python
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]
```
#### remove()
- Removes the first item from the list whose value is equal to the specified value
- Raises a ValueError if the item is not found
```python
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]
```
#### pop()
- Removes and returns the item at the specified position
- If no index is specified, removes and returns the last item
```python
my_list = [1, 2, 3]
item = my_list.pop()
print(item)  # Output: 3
print(my_list)  # Output: [1, 2]
```
#### clear()
- Removes all items from the list
```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
```
#### index()
- Returns the index of the first item whose value is equal to the specified value
- Raises a ValueError if the item is not found
```python
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1
```
#### count()
- Returns the number of times the specified value appears in the list
```python
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2
```
#### sort()
- Sorts the list in ascending order by default
- You can specify the `reverse` parameter to sort in descending order
```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

my_list.sort(reverse=True)
print(my_list)  # Output: [3, 2, 1]
```
#### reverse()
- Reverses the elements of the list in place
```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
```
#### copy()
- Returns a shallow copy of the list
```python
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]
```
#### list() Constructor
- Creates a new list
```python
# Using the list constructor
my_list = list([1, 2, 3])
print(my_list)  # Output: [1, 2, 3]
```
#### List Comprehension
- List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc
```python
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
---


# 03 Tuple
- immutable
- Faster than lists
- Can be used as keys in dictionaries, while lists can't
- To create a tuple with a single element, we have to include the final comma, Without the comma, Python treats it as a string in parentheses
```python
t = ("tuples", "are", "immutable")
print(t[0]) # Output: 'tuples'
```

#### count()
- Returns the number of times a specified value appears in the tuple
```python
my_tuple = (1, 2, 3, 2, 4, 2)
count = my_tuple.count(2)
print(count)  # Output: 3
```
#### index()
- Returns the index of the first occurrence of the specified value
- Raises a ValueError if the value is not found
```python
my_tuple = (1, 2, 3, 2, 4, 2)
index = my_tuple.index(3)
print(index)  # Output: 2
```
#### Slicing
```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:3])  # Output: (2, 3)
print(my_tuple[:4])   # Output: (1, 2, 3, 4)
```
#### Concatenation
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5)
```
#### Repetition
```python
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)
```
#### Tuple Unpacking
```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```
---


# 04 Dictionary
#### dict() Constructor
- Creates a new dictionary
```python
# Using the dict constructor
my_dict = dict(name='Alice', age=25)
print(my_dict)  # Output: {'name': 'Alice', 'age': 25}
```
#### accessing values
- Access the value associated with a specific key
```python
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])  # Output: 'Alice'
print(my_dict.get('age'))  # Output: 25
```
#### keys()
- Returns a view object that displays a list of all the keys
```python
my_dict = {'name': 'Alice', 'age': 25}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age'])
```
#### values()
- Returns a view object that displays a list of all the values
```python
my_dict = {'name': 'Alice', 'age': 25}
values = my_dict.values()
print(values)  # Output: dict_values(['Alice', 25])
```
#### items()
- Returns a view object that displays a list of a dictionary’s key-value tuple pairs
```python
my_dict = {'name': 'Alice', 'age': 25}
items = my_dict.items()
print(items) 
# Output: dict_items([('name', 'Alice'), ('age',25)])
```
#### update()
- Updates the dictionary with the elements from another dictionary object or from an iterable of key-value pairs
```python
my_dict = {'name': 'Alice', 'age': 25}
my_dict.update({'age': 26, 'city': 'Wonderland'})
print(my_dict) 
# Output: {'name': 'Alice', 'age': 26, 'city': 'Wonderland'}
```
#### pop()
- Removes and returns the value for the specified key
- If the key is not found, it raises a KeyError
```python
my_dict = {'name': 'Alice', 'age': 25}
age = my_dict.pop('age')
print(age)  # Output: 25
print(my_dict)  # Output: {'name': 'Alice'}
```
#### popitem()
- Removes and returns the last inserted key-value pair as a tuple
```python
my_dict = {'name': 'Alice', 'age': 25}
item = my_dict.popitem()
print(item)  # Output: ('age', 25)
print(my_dict)  # Output: {'name': 'Alice'}
```
#### setdefault()
- Returns the value of the specified key
- If the key does not exist, insert the key with the specified value
```python
my_dict = {'name': 'Alice'}
age = my_dict.setdefault('age', 25)
print(age)  # Output: 25
print(my_dict)  # Output: {'name': 'Alice', 'age': 25}
```
#### clear()
- Removes all elements from the dictionary
```python
my_dict = {'name': 'Alice', 'age': 25}
my_dict.clear()
print(my_dict)  # Output: {}
```
#### copy()
- Returns a shallow copy of the dictionary
```python
my_dict = {'name': 'Alice', 'age': 25}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 25}
```
#### fromkeys()
- Creates a new dictionary from the given sequence of keys, with the specified value for all keys
```python
keys = ['name', 'age', 'city']
value = None
new_dict = dict.fromkeys(keys, value)
print(new_dict)  
# Output: {'name': None, 'age': None, 'city': None}
```
#### in operator
- Checks if a key exists in the dictionary
```python
my_dict = {'name': 'Alice', 'age': 25}
print('name' in my_dict)  # Output: True
print('city' in my_dict)  # Output: False
```
#### Dictionary Comprehension
```python
keys = ['m', 'a', 'l', 'y']
values = [2, 4, 3, 2]
myDict = { k:v for (k,v) in zip(keys, values)}
print(myDict)

# {'m': 2, 'a': 4, 'l': 3, 'y': 2}
```
---


# 05 Set
#### add()
```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```
#### remove()
- Removes the specified element from the set
- Raises a KeyError if the element is not found
```python
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4}
```
#### discard()
- Removes the specified element from the set if it is present
- Does not raise an error if the element is not found
```python
my_set = {1, 2, 3, 4}
my_set.discard(3)
my_set.discard(5)  # No error raised
print(my_set)  # Output: {1, 2, 4}
```
#### clear()
```python
my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set)  # Output: set()
```
#### copy()
```python
my_set = {1, 2, 3, 4}
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3, 4}
```
#### pop()
- Removes and returns an arbitrary element from the set
- Raises a KeyError if the set is empty
```python
my_set = {1, 2, 3, 4}
element = my_set.pop()
print(element)  # Output: (An arbitrary element from the set)
print(my_set)  # Output: Set without the popped element
```
#### union()
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
```
#### intersection()
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
```
#### difference()
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
```
#### symmetric_difference()
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```
#### update()
- union update
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
```
- intersection_update()
- difference_update()
- symmetric_difference_update()
---


# Functions

#### Abstraction Mechanism & Top-down design
```python
def main():
    name = input("Enter your name: ")
    print(greet(name))

def greet(name):
    return f"Hello, {name}!"

main()
```

#### Recursive Functions
```python 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 120
```


#### kwargs
- kwargs allows you to pass keyworded variable length of arguments to a function
```Python
def test_kwargs(farg, **kwargs):
	print ("formal arg:", farg)
	for key in kwargs:
		print ("another keyword arg: %s: %s" % (key, kwargs[key]))

test_kwargs(farg=1, myarg2="two", myarg3=3)
```
#### args 
- is used to send a non-keyworded variable length argument list to the function
```Python
def test_args(first, second, third, *args):
	print("First: %s" % first)
	print("Second: %s" % second)
	print("Third: %s" % third)
	print("And all the rest... %s" % list(args))

test_args('one','two','three','1','2','3','4')
```

#### Lambda functions
- A lambda is an anonymous function
- It has no name of its own, but contains the names of its arguments as well as a single expression
- `lambda <argname-1, ..., argname-n>: <expression>`
```python
# Lambda function to add two numbers
add = lambda x, y: x + y

result = add(3, 5)
print(result)  # Output: 8
```

#### Higher order functions
- Higher-order function expects a function and a set of data values as arguments
- Separates the task of transforming each data value from the logic of accumulating the results
#### 01 map 
- his process applies a function to each value in a sequence (such as a list, a tuple, or a string) and returns a new sequence of the results
```python
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)

# [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
```
#### 02 filtering
- A function called a predicate is applied to each value in a list. If the predicate returns True , the value passes the test and is added to a filter object (similar to a map object). Otherwise, the value is dropped from consideration
```python 
def odd(n):
	return n % 2 == 1
	
list(filter(odd, range(10)))

# [1, 3, 5, 7, 9]
```
#### 03 Reduce
- Take a list of values and repeatedly apply a function to accumulate a single data value
```python
from functools import reduce
def multiply(x, y): return x * y
data = [1, 2, 3, 4]
print(reduce(add, data))
# 24
```
---


## Text files
- Software object that stores data on a permanent medium
```python
f = open("myfile.txt", 'w')
f.readlines()
f.write("First line.\nSecond line.\n")

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')    # 16

f.seek(5)                       # Go to the 6th byte in the file - 5
f.read(1)                       # b'5'
f.seek(-3, 2)                   # Go to the 3rd byte before the end - 13
f.read(1)                       # b'd'
```

## Date & Time
```python
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S")) # '2024-07-02 10:29:56'
```

## JSON
- JSON (JavaScript Object Notation) is a lightweight data interchange format
- Python provides a built-in package called `json` to work with JSON data
```python
import json

# Converting Python object to JSON string
data = {
		name': 'Alice', 
		'age': 25
}
json_data = json.dumps(data)
print(json_data)

# Converting JSON string to Python object
json_str = '{"name": "Bob", "age": 30}'
data = json.loads(json_str)
print(data)
```
---

# Introduction to Graphics
- Graphics involve the representation and display of geometric shapes in two and three dimensions, as well as image processing

#### Turtle Graphics
- It provides a visual representation by moving a "turtle" around the screen to create drawings
- **Turtle State** : The position, heading (direction), pen color, and pen state (up or down)
- `setHeading(degrees)` 0(E), 90(N), 180(W), 270(S)

#### Basic Turtle Operations
1. **Moving the Turtle**
    - `forward(distance)`: Moves the turtle forward by the specified distance
    - `backward(distance)`: Moves the turtle backward by the specified distance
    - `left(angle)`: Turns the turtle left by the specified angle
    - `right(angle)`: Turns the turtle right by the specified angle
2. **Pen Control**
	- `penup()`: Lifts the pen so that moving the turtle does not draw a line
	- `pendown()`: Lowers the pen so that moving the turtle draws a line
	- `pencolor(color)`: Sets the color of the pen
	- `pensize(size)`: Sets the width of the pen
3. **Setting the Turtle's Attributes**
	- `shape(shape)`: Sets the shape of the turtle (e.g., "turtle", "arrow", "circle")
	- `speed(speed)`: Sets the speed of the turtle (1 to 10)
4. **Filling Shapes**
	- `begin_fill()`: Starts filling the shape
	- `end_fill()`: Ends filling the shape

#### Drawing Two-Dimensional Shapes
- eg : triangle.py
```python
import turtle

def draw_triangle(t, length):
    for _ in range(3):
        t.forward(length)
        t.left(120)

# Setup turtle
t = turtle.Turtle()
draw_triangle(t, 100)
turtle.done()
```
#### Colors and the RGB System
- Colors in graphics are often represented using the RGB (Red, Green, Blue) system, where each color component can range from 0 to 255

```python 
import turtle

t = turtle.Turtle()
t.pencolor('red')  # Red
t.fillcolor('green')  # Green
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
turtle.done()
```

### Image Processing
- Involves capturing, representing, and manipulating images

- Rotate an image
- Convert an image from color to grayscale
- Apply color filtering to an image
- Highlight a particular area in an image
- Blur all or part of an image
- Sharpen all or part of an image
- Control the brightness of an image
- Perform edge detection on an image
- Enlarge or reduce an image’s size
- Apply color inversion to an image
- Morph an image

**Convert an image from color to grayscale**
```python
def grayscale(image):
    """Converts the argument image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

# Test the function
from images import Image
image = Image("example.gif")
grayscale(image)
image.draw()
```
#### Image Methods
---
#### open()
```python
from PIL import Image
# from images import Image

# Open an image file
img = Image.open('example.jpg')
img.show()
```
#### Image(filename)
```python
from PIL import Image

# Open an image file
img = Image.open('example.jpg')
img.show()
```
#### getWidth() & getHeight()
```python
height = image.getHeight()
print(f"Height: {height}")

height = image.getHeight()
print(f"Height: {height}")
```
#### getPixel(x, y)
- Returns the RGB color value of the pixel at the specified (x, y) position
```python
pixel = image.getPixel(0, 0)
print(f"Pixel at (0, 0): {pixel}")
```
#### setPixel(x, y, (r, g, b))
- Sets the color of the pixel at the specified (x, y) position to the given RGB value
```python
image.setPixel(0, 0, (255, 0, 0))  
# Set the pixel at (0, 0) to red
image.draw()
```
#### draw()
- Displays the image
```python
image.draw()
```
#### save(filename)
```python
image.save("output.gif")
```
#### copy()
```python
image_copy = image.copy()
image_copy.draw()
```


### Graphical User Interfaces (GUIs)
- GUIs allow users to interact with software through graphical elements like buttons, icons, and menus, rather than text commands

```python
import tkinter as tk

def on_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()
root.mainloop()
```
---
# Python OOP

| Object-oriented Programming (OOP)            | Procedure-oriented Programming (POP)                  |
| -------------------------------------------- | ----------------------------------------------------- |
| Encapsulates data and functions into objects | Focuses on functions or procedures to operate on data |
| Provide Data hiding                          | Doesn't provide, proper way for Data binding          |
| C++, C#, Java, .Net, Python                  | C, Fortran, Pascal, VB                                |
### Overview of OOP (Object Oriented Programming)
---
- Python is a multi-paradigm programming language (POP & OOP)
```python
def add(a, b):
    return a + b
result = add(5, 3)


class Calculator:
    def add(self, a, b):
        return a + b
calc = Calculator()
result = calc.add(5, 3)

```


### 01 class & object
- Class is a collection of data (variables) & methods
```python
	class <class name>(<parent class name>):
```
- Object is an instance of a class
```python
<object name> = <class name>
```

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"Car: {self.brand} {self.model}"
        
my_car1 = Car("Toyota", "Corolla")
my_car2 = Car("Mahindra", "Thar")
print(my_car1.display())
print(my_car2.display())
```

#### Constructor
- Special method `__init__` to initialize objects
- **Non-parameterized Constructor**
	- Uses when we do not want to manipulate the value 
	- The constructor that has only self as an argument
- **Parameterized Constructor**
	- Has multiple parameters along with the self
	- `self.parameter` required 
#### Accessor & Mutator
-  Methods that access object attributes - Accessor
-  Methods that modify object attributes - Mutator

```python 
class Circle:
    def __init__(self, radius):    # constructor
        self.__radius = radius     # private attribute

    def get_radius(self):          # accessor
        return self.__radius

    def set_radius(self, radius):  # mutator
        self.__radius = radius
        
circle = Circle(5)
print(circle.get_radius())  # 5
circle.set_radius(10)
print(circle.get_radius())  # 10
```


### 02 Data Encapsulation
- Restrictions imposed on the access to methods and variables
- The attribute `__balance` is defined with double underscores. This makes it a private attribute
- When you define a private attribute `__balance`, Python internally changes its name to `_ClassName__balance`. This is done to avoid attribute name conflicts in subclasses
```python
class BankAccount:
	def __init__(self, balance): # constructor
		self.__balance = balance

	def deposit(self, amount):   # mutator 
		self.__balance += amount

	def getBalance(self):        # accessor
		return self.__balance

account = BankAccount(1000)
# print(account._BankAccount__balance) : Output: 1000
account.deposit(2000)
print(account.getBalance()) # 3000
```


### 03 Inheritance
- Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class)
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy says Woof
```

#### Method Resolution Order (MRO)
- Order in which Python looks for a method in a hierarchy of classes
- MRO works in a depth first left to right way
- eg - Multiple-inheritance

#### Super() function
- Make the child class inherit all the methods and properties from its parent
- By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent


### 04 Polymorphism 
- object of a class can have many different forms to respond in different ways to any message or action
	- Operator Overloading
	- Method Overloading
	- Method Overriding
```python
class Bird:
    def speak(self):
        return "Bird is making a sound."

class Parrot(Bird):
    def speak(self):
        return "Parrot is talking."

class Sparrow(Bird):
    def speak(self):
        return "Sparrow is chirping."
        
def make_bird_speak(bird):
    print(bird.speak())
    
parrot = Parrot()
sparrow = Sparrow()

make_bird_speak(parrot)  # Parrot is talking.
make_bird_speak(sparrow)  # Sparrow is chirping.
```


### 05 Abstraction
- Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object
- It is achieved using abstract classes and interfaces

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage
shapes = [Rectangle(10, 20), Circle(15)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
```


### Exception Handling
- `try` block contains the code that might raise an exception
- `except` blocks handle specific exceptions
- `else` block executes if no exceptions are raised
- `finally` block executes regardless of whether an exception was raised
- `raise` An exception can be raised forcefully

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

# Usage
divide(10, 2)
divide(10, 0)
divide(10, 'a')
```

- ZeroDivisionError
- FileNotFoundError
- NameError 
- TypeError 
- ValueError
- NotImplementedError : When an object is supposed to support an operation but it has not been implemented yet
- User-Defined Exception
```python
class invalidAge(Exception):
	def display(self):
		print("Age cannot be below 18 ")

try:
	age = int(input("Enter the Age :"))
	if age < 18:
		raise invalidAge()
except invalidAge as a:
	a.display()
else:
	print(name, "Congratulations !!! You can enter the CLUB")
```
---
# Some Py-Modules
## 01 py_compile
- **Automatic Compilation** : Python compiles scripts to bytecode before running them, creating `.pyc` files
- **Manual Compilation** : Use `py_compile` and `compileall` modules
```python
import py_compile
```

```Python
py_compile.compile('abc.py')
```

```shell
python -m compileall .
```
#### `__init__.py` File
- Required to make Python treat directories as packages
- Can be empty or execute initialization code for the package
---


## 02 RE
- Used to filter text or text strings in programming languages.
- Useful for data cleaning, wrangling, and performing various text-processing tasks in data science & machine learning

#### Purposes
- **Parsing** : Identifying & extracting text matching certain patterns
- **Searching** : Locating substrings with specific criteria
- **Replacing** : Substituting matching substrings with other strings
- **Splitting** : Dividing strings based on matching patterns
- **Validation** : Checking if text meets specified criteria
#### Identifiers
- \d = any number
- \D = anything but a number
- \s = space
- \S = anything but a space
- \w = any letter
- \W = anything but a letter
- . = any character, except for a new line
- \b = space around whole words
- \. = period. must use backslash, because . normally means any character

```python
import re
```

```python
text = "start learning" 
pattern = re.compile("start") # Compiles a regex pattern into a regex object
```

```python
result = pattern.match(text)  # Checks for a match only at the beginning of the string
```

```python
line = "He is a German called Mayer" 
if re.search(r"M[ae][iy]er", line): # Searches the entire string for a match
	print("I found one!")
```

```python
text = "Mona and Reena are two sisters, of age 12 and 15 respectively" 
ages = re.findall(r'\d{1,3}', text) 
print(ages)                        # ['12', '15']
```

```python
re.split(r'\s*', 'here are some words') 
# Output: ['here', 'are', 'some', 'words']
```

```python
text = "Cats are smarter than dogs" 
re.sub(r'dogs', 'cats', text)      # Output: "Cats are smarter than cats"
```

```python
matches = re.finditer(r"([a-zA-Z]+) \d+", "June 24, August 9, Dec 12") 
for match in matches: 
	print("Match at index: %s, %s" % (match.start(), match.end()))

# Match at index: 0, 7
# Match at index: 9, 17
# Match at index: 19, 25
```

```python
match.group()
match.start()
match.end()
```
---


## 03 PDB
- `pdb` stands for Python Debugger
- It is a built-in module in Python used for interactive debugging of Python programs
- It allows you to set breakpoints, step through code, inspect variables, and evaluate expressions at runtime
```python
import pdb
```

```python
(Pdb) help
(Pdb) help clear
pdb.help()      # Prints general help
```

```python
(Pdb) where
(Pdb) bt        # Prints a stack trace, with the most recent frame at the bottom
```

```python
(Pdb) down      # Move the current frame one level down in the stack trace
```

```python
(Pdb) up        # Move the current frame one level up in the stack trace
```

```python
(Pdb) break 10  # Sets a breakpoint at the specified line number or function
(Pdb) break mymodule.py:10
```

```python
(Pdb) clear     # Clears breakpoints
(Pdb) clear 1
```

```python
(Pdb) disable 1
```

```python 
(Pdb) enable 1
```

```python
(Pdb) step      # Execute the current line, stop at the first possible occasion
```

```python
(Pdb) next      # Continue execution until the next line in the current function is reached
```

```python
(Pdb) jump 20   # Set the next line that will be executed
```

```python
(Pdb) list 5,10 # List source code for the current file
```

```python 
(Pdb) display a # Use to display the value of a when it changes
```
---


## 04 OS
- The OS module in python provides functions for interacting with the OS
- Comes under Python’s standard utility modules
- Provides a portable way of using OS dependent functionality
```python
import os 
```

```python
os.name # Name of the operating system-dependent module
```

```python
print(os.getcwd())  # Current working directory path
```

```python
print(os.listdir('.')) # List of files and directories in the current directory
```

```python
os.chdir('..') # Changes to the parent directory
```

```python
os.mkdir('test_directory') # A new directory named 'test_directory' is created
```

```python
os.remove('test_file.txt') # The file 'test_file.txt' is removed
```

```python
os.rename('old.txt','new.txt') # 'old.txt' is renamed to 'new.txt'
```
---


## 05 Sys 
- Provides functions and variables used to manipulate different parts of the Python runtime environment

```python
import sys
```

```Python
sys.ps1  # '>>> '
sys.ps2  # '... '
```

```python
print(sys.argv[0], sys.argv[1], sys.argv[2])
$ python script.py arg1 arg2
# Output: script.py arg1 arg2
```

```python
sys.maxsize # 9223372036854775807
```

```python
sys.stdout = open('output.txt', 'w') 
sys.stdin, sys.stderr
```

```python
sys.getsizeof(obj) # size of an object in bytes
```

```python
sys.path # path to the current-directory
```

```python
sys.platform # 'linux'
```

```python
sys.version
# '3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]'
```

```python
sys.platform # 'linux'
```

```python
sys.exit(0)
```
---


## 06 NumPy (Numerical Python)
- Library that supports large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays
#### ndarray 
- The most important object defined in NumPy is an N-dimensional array type
- It describes the collection of items of the same type
- Each element in ndarray is an object of data-type object (called dtype)
```python
import numpy as np
```

```python
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)

[[1 2 3]
 [4 5 6]]
```

```python
A = np.arange(10)
# [0 1 2 3 4 5 6 7 8 9]
```

```python
B = np.linspace(0, 1, 5)
# [0.   0.25 0.5  0.75 1.  ]
```

```python
C = np.random.randint(100, size=5)
# [25 62 24 81 39]  # This will vary each time
```

```python
D = np.random.choice([3,5,6,7,9,2], size=(3,5))
[[3 2 5 2 6]
[5 9 3 6 9]
[5 6 9 3 3]]
```

```python
E = np.random.shuffle([1,2,3,4,5])
# [4 1 3 5 2]
```

```python
A = np.array([1, 2, 3])
B = A + 10
print(B)
# [11 12 13]
```

```python
B = A * 2
print(B)
# [2 4 6]
```

```python
A = np.arange(10)
print(E[2:5])
# [2 3 4]
```
#### Matrix Operations
- Addition `A + B`
- Subtraction `A - C`
- Multiplication (Element-wise matrix multiplication or the Hadamard product) `A * B`
- Transpose `A.T or A.transpose()`
- Inverse `inv(A)`
- Trace `trace(A)`
- Determinant `det(A)`
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)
print(C)

[[19 22]
 [43 50]]
```

#### ndarray Object – Parameters
#### ndarray.ndim
- The number of dimensions (axes) of the array
```python
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.ndim)
# 2
```
#### ndarray.shape
- For a matrix with `n` rows and `m` columns, the shape will be `(n, m)`
```python
B = np.array([[1, 2, 3], [4, 5, 6]])
print(B.shape)
# (2, 3)
```
#### ndarray.size
- The total number of elements in the array
```python
C = np.array([[1, 2, 3], [4, 5, 6]])
print(C.size)
# 6
```
#### ndarray.dtype
- The data type of the elements in the array
```python
D = np.array([1, 2, 3])
print(D.dtype)
# int64 - This may vary depending on the platform
```
#### ndarray.itemsize
- The size (in bytes) of each element in the array
```python
E = np.array([1, 2, 3], dtype=np.int32)
print(E.itemsize)
# 4
```
#### ndarray.nbytes
- The total number of bytes consumed by the elements of the array
```python
F = np.array([1, 2, 3], dtype=np.int32)
print(F.nbytes)
# 12
```
#### ndarray.T
- The transposed array (swapping rows and columns)
- Equivalent to `ndarray.transpose()`
```python
G = np.array([[1, 2, 3], [4, 5, 6]])
print(G.T)

[[1 4]
 [2 5]
 [3 6]]
```
#### Broadcasting
- Ability of NumPy to treat arrays of different shapes during arithmetic operations
- If the dimensions of two arrays are dissimilar, operations on arrays of non-similar shapes is still possible in NumPy
- The smaller array is broadcast to the size of the larger array so that they have compatible shapes
---


## 07 matplotlib
- Plotting library for creating static, animated, and interactive visualizations in Python
- Grids and Legends
- Bar plot `plt.bar(x,y)`
- Histogram `plt.hist(var)`
- Scatter plot `plt.scatter(x,y`
- Stem plot `plt.stem(x, y,use_line_collection=True)`
- Pie Plot `pie(data)`
- Subplots with in the same plot `subplot(2,2,1)`
- Ticks in Plot : Ticks are the values used to show specific points on the coordinate axis `plt.xticks(np.arange(start, end, tick))`
```python
import matplotlib.pyplot as plt
```

```python
plt.plot(x, y, label='line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
```
---


## 08 Pandas (Panal Data and Python Data Analysis)
- Python package that offers various data structures and operations for manipulating numerical data and time series
- Two data structure for manipulating data
	- Series
	- DataFrame
- **DataFrame Object** : 2D, size-mutable, potentially heterogeneous tabular data
- **Series Object** : 1D, labeled array capable of holding any data type
- **Data Alignment** : Automatic data alignment with labeled data
- **Missing Data Handling** : Gracefully handles missing data
- **Reshaping** : Flexible reshaping and pivoting of datasets
- **Group By** : Split-apply-combine methodology for data aggregation and transformation
- **Time Series** : Powerful tools for working with time-series data
```python
import pandas as pd
```
#### Series
- Array-like object containing an array of data and an associated array of data labels, called its index
- Pandas Series is nothing but a column in an excel sheet
```python
# Creating a Series
data = [1, 3, 5, 7, 9]
index = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index)
print(series)
# Output
a    1
b    3
c    5
d    7
e    9
dtype: int64
```
##### Attributes & Methods of Series
```python
# Creating a Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
```

```python
series[0]   # First element: 10
series[2:4] # 20 30
```

```python
series.head() # default 5
0 10 
1 20 
2 30 
3 40 
4 50 
dtype: int64
```

```python
series.tail()
0 10
1 20 
2 30
3 40
4 50 
dtype: int64
```

```python
series.axes # [RangeIndex(start=0, stop=5, step=1)]
```

```python
series.dtype # `int64`
```

```python
series.empty # False 
```

```python
series.ndim # 1
```

```python
series.size # 5
```

```python
series.values # [10 20 30 40 50]
```

```python
series.index  # RangeIndex(start=0, stop=5, step=1)
```

```python
# Arithmetic Operations
series + 10
0 20 
1 30 
2 40 
3 50 
4 60
series * 2
0 20 
1 40 
2 60 
3 80 
4 100
```

```python
np.sqrt(series)
0 3.162278 
1 4.472136 
2 5.477226 
3 6.324555 
4 7.071068
```

```python
# Conditional Selection
series[series > 30]
3 40 
4 50
```

```python
# Series Alignment
series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
series1 + series2

a NaN 
b 6.0 
c 8.0 
d NaN 
dtype: float64
```

```python
# Handling Missing Data
data = {'a': 1, 'b': 2, 'c': None}
series = pd.Series(data)

series.isna()
a False 
b False 
c True 
dtype: bool

series.fillna(0)
a 1.0 
b 2.0 
c 0.0 
dtype: float64
```

#### DataFrame
- A `DataFrame` is a two-dimensional labeled data structure with columns of potentially different types
#### Creating a DataFrame
```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print(df)
```

```python
      Name  Age         City
0    Alice   24     New York
1      Bob   27  Los Angeles
2  Charlie   22      Chicago
3    David   32      Houston
```
#### Dealing with Rows & Columns
- add, delete & rename rows and columns in a DataFrame
```python
df['Country'] = 'USA'
print(df)
```

```python
      Name  Age         City Country
0    Alice   24     New York     USA
1      Bob   27  Los Angeles     USA
2  Charlie   22      Chicago     USA
3    David   32      Houston     USA
```

```python
df = df.drop('Country', axis=1)
print(df)
```

```python
      Name  Age         City
0    Alice   24     New York
1      Bob   27  Los Angeles
2  Charlie   22      Chicago
3    David   32      Houston
```

```python
df = df.rename(columns={'Name':'Full Name', 'City':'Location'})
print(df)
```

```python
   Full Name  Age     Location
0      Alice   24     New York
1        Bob   27  Los Angeles
2    Charlie   22      Chicago
3      David   32      Houston
```

```python
new_row = {'Full Name': 'Eve', 'Age': 29, 'Location': 'Miami'}
df = df.append(new_row, ignore_index=True)
print(df)
```

```python
   Full Name  Age     Location
0      Alice   24     New York
1        Bob   27  Los Angeles
2    Charlie   22      Chicago
3      David   32      Houston
4        Eve   29        Miami
```

```python
df = df.drop(0)
print(df)
```

```python
   Full Name  Age     Location
1        Bob   27  Los Angeles
2    Charlie   22      Chicago
3      David   32      Houston
4        Eve   29        Miami
```
#### Indexing & Selecting Data
- Select data by label or by position using `.loc` and `.iloc`.
```python
df.loc[1:3, ['Full Name', 'Age']] 
# df.iloc[2:4 ,['Full Name', 'Age']]
```

```python
   Full Name  Age
1        Bob   27
2    Charlie   22
3      David   32
```
#### Working with Missing Data
```python
df.at[1, 'Age'] = None
print(df.isna())
```

```python
   Full Name    Age  Location
1      False   True     False
2      False  False     False
3      False  False     False
4      False  False     False
```

```python
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)
```

```python
   Full Name        Age     Location
1        Bob  27.666667  Los Angeles
2    Charlie  22.000000      Chicago
3      David  32.000000      Houston
4        Eve  29.000000        Miami
```

```python
df.at[1, 'Age'] = None
df = df.dropna()
print(df)
```

```python
   Full Name   Age Location
2    Charlie  22.0  Chicago
3      David  32.0  Houston
4        Eve  29.0    Miami
```
#### Iterating over Rows and Columns
```python
for index, row in df.iterrows():
    print(index, row['Full Name'], row['Age'])
```

```python
2 Charlie 22.0
3 David 32.0
4 Eve 29.0
```

```python
for column in df:
    print(column, df[column].values)
```

```python
Full Name ['Charlie' 'David' 'Eve']
Age [22. 32. 29.]
Location ['Chicago' 'Houston' 'Miami']
```
#### CSV Files
- **Pandas** is a powerful data manipulation and analysis library for Python
- **Manipulating Data** : Performing operations like filtering, grouping, and aggregating
- **Processing Data** : Applying functions to process data
```python
import pandas as pd
df.to_csv('studdata.csv')
data = pd.read_csv('file.csv')
```
