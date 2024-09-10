# Py-Extras

# Py-Name Mangling

- Name mangling is a technique used to avoid name conflicts in classes
- When you define a class attribute with a name that starts with two underscores and does not end with two underscores, Python alters the name of the attribute in a way that makes it harder to accidentally override in subclasses
- This is done by prefixing the name of the attribute with `_ClassName__`

### How Name Mangling Works

```python
class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        return "This is a private method"

    def access_private_method(self):
        return self.__private_method()

# Creating an instance of MyClass
obj = MyClass()

# Trying to access the private attribute and method directly
print(obj.__private_attribute)  # This will raise an AttributeError
print(obj.__private_method())   # This will raise an AttributeError

# Accessing the private attribute and method using the mangled name
print(obj._MyClass__private_attribute)  # This will print: I am private
print(obj._MyClass__private_method())   # This will print: This is a private method

# Accessing the private method through a public method
print(obj.access_private_method())  # This will print: This is a private method
```

### Explanation

1. **Private Attribute and Method**:
    - `self.__private_attribute` and `self.__private_method` are defined with double underscores
    - These are intended to be private and not accessible directly from outside the class

2. **Name Mangling**:
    - Python changes `__private_attribute` to `_MyClass__private_attribute`
    - Python changes `__private_method` to `_MyClass__private_method`

3. **Accessing Mangled Names**:
    - Accessing `obj.__private_attribute` or `obj.__private_method()` directly will raise an `AttributeError` because these names are mangled
    - You can access them using their mangled names: `obj._MyClass__private_attribute` and `obj._MyClass__private_method()`

4. **Public Method Access**:
    - The public method `access_private_method` can call the private method internally without issues

### Use Cases
- **Encapsulation**: Name mangling helps in encapsulating class attributes and methods, making it clear that these are meant for internal use within the class
- **Avoiding Conflicts**: It prevents accidental name conflicts in subclasses that might override attributes or methods

### Limitations
- **Not True Privacy**: Name mangling is not a strict access control mechanism. It's more of a convention and a way to avoid accidental access
- **Code Readability**: Overuse of double underscores can make code harder to read and maintain. It's often better to use a single underscore (`_`) to indicate that an attribute or method is intended for internal use without invoking name mangling


# Py-Methods

# 1. Instance Methods
- Instance methods are the most common type of method in Python classes
- They are used to manipulate the instance-specific data (i.e., attributes) of the class.
- The first parameter of an instance method is always `self`, which refers to the instance of the class

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self, increment):
        self.value += increment
        return self.value

obj = MyClass(10)
print(obj.instance_method(5))  # Output: 15
```


# 2. Class Methods
- Class methods are methods that are bound to the class and not the instance of the class
- They can modify the class state that applies across all instances of the class
- To define a class method, you use the `@classmethod` decorator
- The first parameter of a class method is always `cls`, which refers to the class itself

#### When to use Class Methods
1. When you need to access or modify the class state
2. When you want to provide an alternative constructor

```python
class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def class_method(cls, value):
        cls.class_variable = value

    @classmethod
    def from_string(cls, string):
        value = int(string)
        return cls(value)

# Using class method to modify class state
MyClass.class_method(10)
print(MyClass.class_variable)  # Output: 10

# Using class method as an alternative constructor
obj = MyClass.from_string("20")
print(obj.instance_variable)  # Output: 20
```


# 3. Static Methods
- Static methods are methods that do not modify class or instance state
- They are utility functions that perform a task in isolation
- To define a static method, you use the `@staticmethod` decorator
- Static methods do not take `self` or `cls` as their first parameter

#### When to use Static Methods
1. When you have a method that doesn't interact with class or instance attributes
2. When you want to group related functions in a class for better organization

```python
class MyClass:
    def __init__(self, value):
        self.instance_variable = value

    @staticmethod
    def static_method(x, y):
        return x + y

# Using static method
result = MyClass.static_method(5, 10)
print(result)  # Output: 15
```


# 4. Magic methods (dunder methods)
- (short for "**double underscore**"), are special methods with double underscores at the beginning and end of their names
- These methods allow you to define how objects of a class behave with respect to built-in operations such as addition, subtraction, printing, and more

### Summary of Magic Methods

- **Initialization and Representation**
  - `__init__(self, ...)`: Initializes a new instance
  - `__str__(self)`: String representation
  - `__repr__(self)`: Official string representation

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value {self.value}"

    def __repr__(self):
        return f"MyClass({self.value})"

obj = MyClass(10)
print(obj)        # Output: MyClass with value 10
print(repr(obj))  # Output: MyClass(10)
```


- **Comparison**
  - `__eq__(self, other)`: Equality
  - `__ne__(self, other)`: Inequality
  - `__lt__(self, other)`: Less than
  - `__le__(self, other)`: Less than or equal to
  - `__gt__(self, other)`: Greater than
  - `__ge__(self, other)`: Greater than or equal to

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

obj1 = MyClass(10)
obj2 = MyClass(20)
print(obj1 == obj2)  # Output: False
print(obj1 < obj2)   # Output: True
```


- **Arithmetic Operations**
  - `__add__(self, other)`: Addition
  - `__sub__(self, other)`: Subtraction
  - `__mul__(self, other)`: Multiplication
  - `__truediv__(self, other)`: True division
  - `__floordiv__(self, other)`: Floor division
  - `__mod__(self, other)`: Modulus
  - `__pow__(self, other)`: Power

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyClass(self.value + other.value)

obj1 = MyClass(10)
obj2 = MyClass(20)
result = obj1 + obj2
print(result)  # Output: 30
```


- **Container Methods**
  - `__len__(self)`: Length
  - `__getitem__(self, key)`: Get item
  - `__setitem__(self, key, value)`: Set item
  - `__delitem__(self, key)`: Delete item
  - `__iter__(self)`: Iteration

```python
class MyClass:
    def __init__(self):
        self.data = {}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

obj = MyClass()
obj['key'] = 'value'
print(obj['key'])  # Output: value
print(len(obj))    # Output: 1
del obj['key']
print(len(obj))    # Output: 0
```


- **Context Management**
  - `__enter__(self)`: Enter context
  - `__exit__(self, exc_type, exc_value, traceback)`: Exit context

```python
class MyClass:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyClass() as obj:
    print("Inside the context")
```


- **Other Magic Methods**
  - `__call__(self, ...)`: Callable objects
  - `__bool__(self)`: Boolean conversion

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x

    def __bool__(self):
        return self.value > 0

obj = MyClass(10)
print(obj(5))      # Output: 15
print(bool(obj))   # Output: True

obj2 = MyClass(0)
print(bool(obj2))  # Output: False
```


# Py-Decorators

- Decorators in Python are a powerful and convenient way to modify the behavior of functions or classes
- They allow you to wrap another function to extend or alter its behavior without modifying the function itself
- A decorator is a function that takes another function (or method) as an argument, adds some functionality, and returns another function
- The basic syntax for decorators involves the `@decorator_name` syntax above the function definition

### 1. Creating a Simple Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

```
Something is happening before the function is called
Hello!
Something is happening after the function is called
```


### 2. Decorators with Arguments

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

```
Something is happening before the function is called
Hello, Alice!
Something is happening after the function is called
```


### 3. Decorators with Return Values

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(3, 4)
print(f"Result: {result}")
```

```
Something is happening before the function is called
Something is happening after the function is called
Result: 7
```


### 4. Using `functools.wraps`
- To preserve the original function’s metadata (such as its name and docstring), you should use the `functools.wraps` decorator inside the decorator

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called")
        return result
    return wrapper

@my_decorator
def say_hello():
    """A simple function to say hello"""
    print("Hello!")

print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: A simple function to say hello
```


### 5. Common Use Cases

1. **Logging**
   ```python
   def log(func):
       @functools.wraps(func)
       def wrapper(*args, **kwargs):
           print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
           result = func(*args, **kwargs)
           print(f"{func.__name__} returned {result}")
           return result
       return wrapper
   ```

2. **Access Control / Authentication**
   ```python
   def requires_authentication(func):
       @functools.wraps(func)
       def wrapper(user, *args, **kwargs):
           if not user.is_authenticated:
               raise Exception("Authentication required")
           return func(user, *args, **kwargs)
       return wrapper
   ```

3. **Caching**
   ```python
   def cache(func):
       cached_results = {}
       @functools.wraps(func)
       def wrapper(*args):
           if args in cached_results:
               return cached_results[args]
           result = func(*args)
           cached_results[args] = result
           return result
       return wrapper
   ```


# 01. **Class Method Decorators**
- Decorators like `@classmethod` and `@staticmethod` are used to define methods that are not bound to an instance of the class but to the class itself or are static, respectively

- **`@classmethod`**: Used for defining a method that receives the class as its first argument instead of an instance

    ```python
    class MyClass:
        class_var = 'Class Variable'

        @classmethod
        def class_method(cls):
            print(f'Class variable is: {cls.class_var}')

    MyClass.class_method()  # Output: Class variable is: Class Variable
    ```


# 02. **Static Method Decorators**
- **`@staticmethod`**: Used for defining a method that does not receive any implicit first argument (neither `self` nor `cls`)

    ```python
    class MyClass:
        @staticmethod
        def static_method():
            print('Static method called')

    MyClass.static_method()  # Output: Static method called
    ```


# 03. **Abstract Method Decorator**
- The `@abstractmethod` decorator from the `abc` module is used to define abstract methods in an abstract base class
- These methods must be implemented by any subclass

```python
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):

    @abstractmethod
    def my_abstract_method(self):
        pass

class ConcreteClass(MyAbstractClass):
    def my_abstract_method(self):
        print("Abstract method implemented")

# concrete_instance = MyAbstractClass()  # This will raise an error
concrete_instance = ConcreteClass()
concrete_instance.my_abstract_method()  # Output: Abstract method implemented
```


# 03. **Property Decorators**
- Property decorators like `@property`, `@<property_name>.setter` and `@<property_name>.deleter` are used to define managed attributes in classes

- **`@property`**: Allows a method to be accessed like an attribute

    ```python
    class MyClass:
        def __init__(self, value):
            self._value = value

        @property
        def value(self):
            return self._value

    obj = MyClass(10)
    print(obj.value)  # Output: 10
    ```

- **`@<property_name>.setter`**: Allows you to define a setter method for the property

    ```python
    class MyClass:
        def __init__(self, value):
            self._value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_value):
            if new_value > 0:
                self._value = new_value
            else:
                raise ValueError("Value must be positive")

    obj = MyClass(10)
    obj.value = 20  # No error
    print(obj.value)  # Output: 20
    # obj.value = -5  # This will raise a ValueError
    ```


# 04. **Decorator for Authorization**
- Decorators can be used to enforce authorization checks
- For instance, ensuring a user has the right permissions to access a function

```python
def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if permission not in user.permissions:
                raise PermissionError("Permission denied")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

class User:
    def __init__(self, permissions):
        self.permissions = permissions

@requires_permission('admin')
def admin_only_function(user):
    print("Admin function executed")

user = User(permissions=['user'])
try:
    admin_only_function(user)
except PermissionError as e:
    print(e)  # Output: Permission denied

user = User(permissions=['admin'])
admin_only_function(user)  # Output: Admin function executed
```


# 05. **Memoization**
- Decorators can be used to cache the results of function calls to avoid repeated computations (i.e., memoization)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def expensive_function(x):
    print(f"Computing {x}")
    return x * x

print(expensive_function(4))  # Output: Computing 4 \n 16
print(expensive_function(4))  # Output: 16 (cached result)
```


# 06. **Timing Execution**
- Decorators can be used to measure the execution time of functions

```python
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(2)
    print("Function finished")

slow_function()  # Output: Function finished \n slow_function took 2.0... seconds
```


# Py-Generators

- Generators in Python are a type of iterable, like lists or tuples
- The key difference is they generate items one at a time and only when requested, instead of storing all items in memory at once
- This can be particularly useful when dealing with large datasets or streams of data

### Key Features of Generators
1. **Lazy Evaluation**
	-  Generators produce items only when requested
	- This is known as lazy evaluation and helps in saving memory and processing time, especially with large datasets

2. **State Retention**
	- Generators maintain their state between calls
	- This means they can remember where they left off and resume generating values from that point

3. **Memory Efficiency**
	- Since generators do not store all values in memory, they are more memory-efficient compared to lists or other collections

### 1. Using Generator Functions
- A generator function is defined like a normal function but uses the `yield` keyword to produce values
- Each call to `yield` produces a value and suspends the function's state until the next value is requested

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Usage
counter = count_up_to(5)
for num in counter:
    print(num)
```

Output:
```
1
2
3
4
5
```

- In this example, the `count_up_to` generator function yields numbers from 1 to `max`
- Each time `yield` is called, it returns the current value of `count` and suspends the function until the next value is requested

### 2. Using Generator Expressions
- Generator expressions are similar to list comprehensions but use parentheses `()` instead of square brackets `[]`
- They produce a generator object that can be iterated over

```python
squares = (x * x for x in range(1, 6))

# Usage
for square in squares:
    print(square)
```

Output:
```
1
4
9
16
25
```


## Common Generator Methods
- **`next(generator)`**
	- Retrieves the next value from the generator
	- If the generator is exhausted, it raises a `StopIteration` exception
  
    ```python
    gen = count_up_to(3)
    print(next(gen))  # Output: 1
    print(next(gen))  # Output: 2
    ```

- **`for item in generator`**
	- Iterates over all values generated
	- This is a more Pythonic way to work with generators

    ```python
    for value in count_up_to(3):
        print(value)
    ```

- **`generator.send(value)`**
	- Sends a value into the generator
	- This requires the generator to have a `yield` expression that can receive a value

    ```python
    def echo():
        while True:
            received = yield
            print(f"Received: {received}")

    gen = echo()
    next(gen)          # Prime the generator
    gen.send("Hello")  # Output: Received: Hello
    ```

- **`generator.throw(exception)`**
	- Raises an exception inside the generator

    ```python
    def error_gen():
        try:
            yield 1
        except ValueError:
            yield 2

    gen = error_gen()
    next(gen)
    gen.throw(ValueError)  # Output: 2
    ```

- **`generator.close()`**
	- Closes the generator, freeing up any resources associated with it

    ```python
    def simple_gen():
        try:
            yield 1
        finally:
            print("Generator closed")

    gen = simple_gen()
    next(gen)
    gen.close()  # Output: Generator closed
    ```

### Use Cases
1. **Processing Large Datasets**: Generators are ideal for processing large files or datasets that do not fit into memory
2. **Streaming Data**: Generators are used to handle data streams, such as reading lines from a file one at a time
3. **Infinite Sequences**: Generators can represent infinite sequences, such as generating an infinite series of numbers
4. **Pipelining**: Generators can be used to create pipelines where data is processed step-by-step


# Py-Virtual Environment

- A Python virtual environment is an isolated environment that allows you to manage dependencies for different projects independently
- This is particularly useful when working on multiple projects with different dependencies or versions of libraries

# 1. Setting Up Python Virtual Environment

1. Step 1: Install `virtualenv` 

```sh
pip install virtualenv
```


2. Step 2: Create a Virtual Environment
- Navigate to your project directory and create a virtual environment

```sh
cd my_project
```

```sh
virtualenv venv
```


3. Step 3: Activate the Virtual Environment

- **On Windows**
  ```sh
  .\venv\Scripts\activate
  ```
- **On macOS/Linux**
  ```sh
  source venv/bin/activate
  ```

- Once activated, your terminal prompt will change to indicate you are now working within the virtual environment


4.  Step 4: Install Packages in the Virtual Environment
- These will be isolated to this virtual environment

```sh
pip install requests
```


5. Step 5: Deactivate the Virtual Environment
- To deactivate and exit the virtual environment

```sh
deactivate
```


# 2. Managing Dependencies

1. Step 1: Freeze Dependencies
- To save the current state of your environment’s dependencies

```sh
pip freeze > requirements.txt
```

2. Step 2: Install Dependencies from a File
- To install dependencies listed in a `requirements.txt` file

```sh
pip install -r requirements.txt
```


# 3. Example Program

1. Step 1: Create a Project Directory
```sh
mkdir my_project
cd my_project
```

2. Step 2: Create and Activate a Virtual Environment
```sh
virtualenv venv
source venv/bin/activate   # On macOS/Linux
# .\venv\Scripts\activate  # On Windows
```

3. Step 3: Install a Package
```sh
pip install requests
```

4. Step 4: Create a Python Script
- Create a file named `example.py` in your project directory 
```python
import requests

response = requests.get('https://api.github.com')
print(response.json())
```

5. Step 5: Run the Python Script
```sh
python example.py
```


# 4. Using `venv` Module (Python 3.3+)
- Python 3.3 and above include the `venv` module, which can be used to create virtual environments

1. Step 1: Create a Virtual Environment
```sh
python3 -m venv myenv
```

2. Step 2: Activate the Virtual Environment
- **On Windows**
  ```sh
  .\myenv\Scripts\activate
  ```
- **On macOS/Linux**
  ```sh
  source myenv/bin/activate
  ```

3. Step 3: Install Packages and Manage Dependencies 
```sh
pip install requests
pip freeze > requirements.txt
pip install -r requirements.txt
```


# 5. Example Program with `venv`

1. Step 1: Create and Activate a Virtual Environment
```sh
python3 -m venv myenv
source myenv/bin/activate  # On macOS/Linux
# .\myenv\Scripts\activate  # On Windows
```

2. Step 2: Install Packages and Run the Script
```sh
pip install requests
python example.py
```


# 6. Additional Tips

- **Checking Virtual Environment:** To check if you are in a virtual environment
  ```python
  import sys
  print(sys.prefix)
  ```
  - If you are in a virtual environment, it will print the path to your virtual environment

- **Using `requirements.txt`:** Always keep your `requirements.txt` file updated, and use it to recreate the environment on other machines or when sharing the project with others

