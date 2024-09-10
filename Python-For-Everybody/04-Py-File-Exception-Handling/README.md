### Introduction to File & Exception Handling
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
