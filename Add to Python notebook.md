ADD TO PYTHON NOTEBOOK


# Reverse find
"""
>>> 'x my string x'.rfind('x')
12
>>> 'x my string x'.rfind('y')
-1

"""

# Percent sign as placeholder in strings
"""
>>> "this is a %s" % 'string'
'this is a string'

>>> "this is %s number %i" % ('string', 1)
'this is string number 1'
"""

# Working with classes very good example
preprocessor.string_tools.File_Path




# Classes and Inheritance
https://www.python-course.eu/python3_inheritance.php

# __str__ method

>>> class Person:
...     def __init__(self, first_name, last_name):
...         self.first_name = first_name
...         self.last_name = last_name
...     # override the base Python function __string__
...     # when an instance of this object is called as a string 
...     # (e.g., with str() or print(), this Person.__str__() will be ...     # executed, instead of str.__str__() from Python's base 
...     # package)
...     def __str__(self):
...         return self.first_name + ' ' + self.last_name
>>> person_1 = Person('John', 'Doe')
>>> person_1
<Person object at 0x000001D069254D68>
>>> str(person_1)
'John Doe'
>>>> print(person_1)
John Doe



## Superclasses

Initializing superclass __init__

>>> class A(B, C):
...    def __init__(self, param):
...        B.__init__(self)
...        C.__init__(self, param)


## Initializing multiple superclasses
>>> class A(B, C):
...    def __init__(self, param):
...        B.__init__(self)
...        C.__init__(self, param)


## Class intheritance and overriding (of methods and ATTRIBUTES)
class Person:

>>>     def __init__(self, first, last):
...         self.firstname = first
...         self.lastname = last
... 
...     def Name(self):
...         return self.firstname + " " + self.lastname
... 
>>> class Employee(Person):
... 
...     def __init__(self, first, last, staffnum):
...         ######## THIS IS THE IMPORTANT PART ###################
...         # __init__ method of Employee class overrides __init__ 
...         # method of Person class (by borrowing its attributes)
...         Person.__init__(self, first, last)
...         self.staffnumber = staffnum
... 
...     def GetEmployee(self):
...         ######## THIS IS THE IMPORTANT PART ###################
...         # self.Name is returned for Employee class, even though it
...         # is an attribute of the Person class!
...         return self.Name() + ", " +  self.staffnumber
... 
>>> x = Person("Marge", "Simpson")
>>> y = Employee("Homer", "Simpson", "1007")
 
>>> print(x.Name())
>>> print(y.GetEmployee())
Marge Simpson
Homer Simpson, 1007

### Overriding
Method overriding allows a subclass to provide a different implementation of a method that is already defined by its superclass or by one of its superclasses. The implementation in the subclass overrides the implementation of the superclass by providing a method with the same name, same parameters or signature, and same return type as the method of the parent class.

class Person:

>>>    def __init__(self, first, last, age):
...        self.firstname = first
...        self.lastname = last
...        self.age = age
...
...    def __str__(self):
...        return self.firstname + " " + self.lastname + ", " + str(self.age)
...    class Employee(Person):
... 
...     def __init__(self, first, last, age, staffnum):
...         # __init__ method of Employee class overrides __init__ 
...         # method of Person class (by borrowing its attributes)
...         super().__init__(first, last, age)
...         self.staffnumber = staffnum
... 
...     def __str__(self):
...         ######## THIS IS THE IMPORTANT PART ###################
...         # __str__() method of Employee class overrides __str__() 
...         # method of Person class
...         return super().__str__() + ", " +  self.staffnumber


>>> x = Person("Marge", "Simpson", 36)
>>> y = Employee("Homer", "Simpson", 28, "1007")

>>> print(x)
>>> print(y)
Marge Simpson
Homer Simpson, 1007

## Overloading
Overloading is the ability to define the same method, with the same name but with a different number of arguments and types. It's the ability of one function to perform different tasks, depending on the number of parameters or the types of the parameters. 

JCL: e.g., if a method does different things for string and list inputs, this is likely called overloading.


# Get index position of a substring
.find() vs .index()
There are two string methods for this, find() and index(). The difference between the two is what happens when the search string isn't found.  find() returns -1 and index() raises ValueError.

"""
myString.find('s')
myString.find('x')
"""

# Number of times a character occurs in a string
>>> nStr = '000123000123'
>>> nStr.count('123')
2

# Python print to file (with newline):
Python's print is the standard "print with newline" function.

Therefore, you can directly do, if you use Python 3.x:
>>> print(c+n, file=data)

if you use Python 2.x:
>>> print  >> data, c+n

# Fluent Interface / *Metamorphic methods*
Python[edit]
In Python returning `self` in the instance method is one way to implement the fluent pattern.

>>> class Poem(object):
>>>     def __init__(self, content):
>>>         self.content = content
>>> 
>>>     def indent(self, spaces):
>>>         self.content = " " * spaces + self.content
>>>         return self
>>> 
>>>     def suffix(self, content):
>>>         self.content = self.content + " - " + content
>>>         return self

>>> Poem("Road Not Travelled").indent(4).suffix("Robert Frost").content
'    Road Not Travelled - Robert Frost'


