# FEM Python Fundamentals

SET UP:
  [Creating Virtual Environments](https://docs.python.org/3/library/venv.html#)

  check version
    python --version
  create a virtual environment
    the -m means run this next command as a module, a virtual environment and name the folder env
    this creates a standalone python interpreter., gurantees we are using the version of python when we created it
    it will not pollute system settings
    python3 -m venv env
  activate that virtual environment (do this every time you enter this specific project)
    source env/bin/activate
  to exit the vurtual environment
    deactivate - [exit the venv](https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv)

What does the above do?

A virtual environment is created on top of an existing python installation (the virtual environement's base). This virtual env. is self contained, and contains the specific python packages, binaries, and libraries to support this particular project.

The environment is conventionlly located in a directory named `.venv` or `venv`. These virtual environments are __not pushed with source control (git)__, and they are disposable and able to be restarted.

Virtual Environments are created using the __venv__ module.

requirements.txt
  This is special file that tells pip which dependencies are needed (to install) for this program to run. Simply, create this file and place each dependency on a separate line.

  Or have pip create one for you: `$ pip freeze > requirements.txt`
  Then when deployed or moved to a new venv, all the dependencies come along: `$ pip install -r requirements.txt`

  For a specific version of a dependency, place a == and the version number after the name of the package


## REPL

To start a REPL from VSCode, `cmd+shift+P`, which opens the command pallete and then type `start repl` and choose to open a teminal repl.

Or, on the terminal prompt, type `python`, to enter. To exit: `ctl D`

### type() dir() and help()

In the REPL,
   type([variable]) reveals the type, string, number, dict, etc
   dir([variable]) lists a directory of commands available for that type
   help([type/method/object]) shows the syntax and what that method does

### Pep 8

The style guide spec for python.

Integers and other simple data types are just objects under the hood.
Variables
  no need to declare, just name a variable and assign it a value

Numbers
  types are `integer` (int), and `float` (float), and `complex` (ex: 42j)

Mathematical Ops
  add a float and int, result type : float
  divide two ints, result type: float

Booleans
  type `bool`

NUll
  in python is `None`

Print
  equivalent to console.log()

3 quotes
  """ means that there are a continuation of strings ending with another """

Formatting a string
  Perferred method is using "f-string" formatting

```python
  >>> name = "Kev"
  ## formatting a string with 'f-string'
  >>> greeting = f"hello, {name}"
  >>> Hello, Kev
```

`print()` prints the contents
`repr()` - is used for debugging
String concatenation is with a "+"
  can not concatenate a number and a string (no type coercion)

Trimming a string (removing whitespace)
  `.strip()` - returns a new string after removing any leading or trialing whitespace
  `.rstrip()` - returns a new string after removing only trailing whitespace
  .`lstrip()` - returns a new string after removing only leading whitespace

Replacing Characters
  `.replace()` - replaces a word or character. pass the word to be replaced and then its replacement value.

## Functions

No curly braces to delineate the code block, python uses indentations
colon, `:` is used directly after the closing paren for the arguments.

default parameters called `keyword arguments`. The arg is assigned a default value in the parens.
default args __come after regualr args__!! unless they are labeled when passing in the function

```python
  def say_greeting_with_name(name, greeting = "hello gov'nor", punctuation = "!"):
    print(f"{greeting}, {name})
  ```

DO NOT pass empty lists (arrays) as a default arg. Instead of the code block popluating the list or mutating the empty list, python will use that same list over and over again. A new one is not instantiated with a new function call. The original will be modified over and over again!!

__Default arguments are evaluated once - when a function is defined__. That means do not use default args that can be mutated.
__No mutable default args!!__
Python Scope is based on indentation/ whitespace

When naming a list, name it in the plural.

## Data Types - Containers and Sequences

### List

The equivalent to arrays in JS. These are mutable.

To create a list:
  [] or list()
Search:
  item in my_list or my_list.index(item) // search is slow __use a set or dict instead__
Common Methods:
  `.len()` - get the length of the list
  `.append()` - add an item to the end
  `.insert(index, item)` - inserts an item at the specified index position
  `.pop()` - remove an item from the end of the list
  `.sort(`) - sorts list in place (fast), mutates the list
  `.sort(reverse=True)` - sorts in descending order, mutates the list
  `.reverse(`) - reverses the list in place
  `.extend(other_list)` - add items from another list
  `in` - ex: item in my_list, boolean check if an item is in the list
  `.index()` -  returns the index of an item in the list
  `.count()` - returns the number of occurances of a value in the list
  `.remove()` - removes first occurance of a value

Sorting

To sort a list without mutating the list, make a copy.
  `sorted(my_list)` - will return a new sorted list in ascending order
  `sorted(my_list, reverse=True)` - returns a new sorted list in descending order

Slicing

This is a way to create sub-lists out of larger lists (strings are also just a list of characters).

Slicing is accomplished using square brackets.

  from the start to end - my_list[7:12]
    - leaving off the first number is equivalent to starting from 0 - my_list[:7]
  or to the end
    - my_list[7:]
  to copy an entire list, just use the colon
    - my_list[:]

Stride or Step
  These are optional thirde arguments that allow skipping elements in the list or even reverse them.

```python

    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    my_list[::2] # move forward by 2, or skip every other index

    [0, 2, 4, 6, 8]

    my_list[::-1] # move backward by 1, and easy way to reverse a list

    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    my_list[1:7:2] # get every other index between 1 and 7

    [1, 3, 5]
```

### List Comprehensions

A more concise method of looping over a list and providing an expression for the loop to evaluate

A way to write an LC is to:

  1. [start with what you are looping over in square brackets] - [for name in names]
  2. move all the way to the left and enter the expression of what you want to extract - [len(name) for name in names]
  3. profit

Syntax: `[expression for item in iterable if condition]`
Conditionals go after the for/in loop and they must evaluate to True or False

### Tuples

Tuples keep track of related but different items. __Tuples are immutable__
Tuples are like a snapshot of data

Search:
 `in` - item in my_tuple,
 `.index(item)` - finds the index of the item in the tuple
  (search is slow, similar to lists)
Creation:
  `() or tuple()` - for creating an empty tuple
  [ You do not need parens to create a tuple, just a sequence of items followed by a comma ]

Can not add or remove values from a tuple (immutable) and they are not sortable

Tuples are good for storing the data for a row of information in a spreadsheet. We don't care about modifying the data, we might just want a read only snapshot.

Quirks about Tuples:
  In order to create a Tuple with a single value, __add a trailing comma__
  If you need to unpack a tuple with a single value, `item, = tupe_with_one_item`, have that trailing comma!!

Because tuples are immutable, we can use them as keys for `sets` and `dicts`

Unpacking Tuples:
  It seems similar to destructuring in JS

  ```python
  CEO = ("Kevin", 54, "Covette ZR1", "Engineer")
  >>>name, age, car, skill = student
  >>> name
  'Kevin'
  >>>car
  'Corvette ZR1'
  ```

If you don't need a value from a Tuple while unpacking, use an _
You can return tuples from functions and use unpacking

```python
def http_status_code():
    return 200, "OK"
>>>code, value = http_status_code()
>>>code
200
>>>value
'OK'
```

### Sets

Only one instance of an item per set, no duplicates, very fast lookup.
Allow you to store other immutable data types in an unsorted way.
Sets can not contain mutable types (lists), that is why each member is hashed.

Creation:
  In order to make a Set, you must be explicit because Sets and Dicts both use {}
  `set() or {item1, item2, item3}` -
Search:
  `in` - checks for membership in the set
Add:
  `.add(item)` - adds an item to the set
  `.update(other_set)` - adds items from another set
Remove:
  `.discard(item)` - removes an item from the set

Items can not be accessed by index (order is not preserved). Sets are not sortable
Sets are mutable, you can add or remove items from a set. BUT!! only pass another set, list, or tuple, not strings!!!
A Set stores the unique hashed value of each member
Can freeze a Set to create an immutable DS

You can De-dup a list by passing it to a set, this will remove duplicates!!

Set Operations:
  `.union(t)` - s | t - creates a new set with all the items fromboth s and t
  `.intersection(t)` - s & t - creates a new set containing __only__ items that are in both s and and also in t
  `.difference(t)` - s ^ t - creates a new set containing items that are not in both s and in t

There are additional operations also, see dir(set)

### Dictionaries

Store data in key/value pairs. Dictionaries are mutable, but keys are not.
Dicts are excellent for accessing data quickly, lookup is very fast,  and __memoization__ (storing a value for later use)

Creation:
  `{} or dict()` - for an empty dict, for a dict with members: `{1: "one", 2: "two", 3: "three"}`
Search:
  `in` - as keys are unique hashes, lookup is fast
  `my_dict[key]` - find a value by key, KeyError if key is not in the dict
  `my_dict.get(key)` - like above but fails silently, can use a second parameter, "default" to return something
  `my_dict.items()` - for all key/ value pairs in a list of tuples
  `my_dict.keys()` - for all keys
  `my_dict.values()` -for all values
Sorting:
  Sorting is by insertion order, items can not be accessed by index, only by key
Updating:
  Update a dict with [] bracket notation and assign it a value. First check if there is a key with the same name or you will overwrite the value.
  `.update(other_dict)` - adds items from another dict into the current one.

  Values can be lists and with list we can add or remove values and not affect the dict or key of that value

  If we want to access a value with a key

### Booleans

1 is True, 0 is False
empty lists, dict, tuples, sets evaulate to False
None is False

`and, or, not` - boolean operators that compare one or more expressions and then determines if they evaluate to True or False

 `a or b` - if a is False, then b, else a
 `a and b` - if a is False, then a is returned, else b is returned
 `not a` - if a is False, then True, else False
  __not__ reverses the boolean value of the arg



### Comparison Operators

`>` - greater than
`<` - less than
`<=` - less than or equal to
`>=` - greater than or equal to
`==` - equals, are values the same
`!=` - not equals, are values not the same

### Equality

Identity - about memory location, not about same value
Pretty much only use `is` to compare value of built in Types of: None, True, False
  `is` - is the same object in memory
  `is not` - is not the same object in memory

Comparing strings is done by comparing ASCII values of each character one by one until a character is found that is a different value, that determines order.

## Looping and Control Flow

LIST
  Loop over a list: `for [variable] in my_list:`
  To get the index also, use `enumerate()`
    `for index, color in enumerate(my_list):`
    This returns a tuple of index, value pairs

Dict
 Still use a for in loop. this returns the values
 To get the keys, use .keys() method
 To get the keys and values, use .items() - returns a list of tuples

Break statements
  Adding a `break` will break out of the current loop

Continue
  Continue goes back to the start of the loop, skipping over any other statements contained in the loop.

Zip
  Using `zip()`  allows looping over two lists at once. With this we can take two lists (one or ints, and one of names) and use these to create a dict of key/value pairs

```python
names = ['Kevin', 'Heather', 'Farrah', 'Jordy', 'Kieran']
ages = [54, 40, 9, 4, 2]
person_info = dict(zip(names, ages))
{'Kevin': 54, 'Heather': 40, 'Farrah': 9, 'Jordy': 4, 'Kieran': 2}
```

  Zip is a generator function, generators can only be run once.

## Python Programs and Files

To run python code in VSCode Terminal, I created a key binding, ctl + cmd + p

Too avoid the missing docstring error, add `""" comment """`, triple quotes to top of file

If you create a module and import it into another file, you must run a `main` method so the code in the imported module does not run also. The __main__ method is only run as a standalone program. Therefore do a `if __name__ == "__main__":` check as a conditional.
__name__ is a special variable set by python that tells it where it was called from. (__name__) is set to the file that it is in.

```python
# name_lib.py

def name_length(name):
    return len(name)

def upper_case_name(name):
    return name.upper()

def lower_case_name(name):
    return name.lower()

if __name__ == "__main__": # this is the "name" check, __name__ is set to the name of the file that it's in, minus the .py
    name = "Nina"
    length = name_length(name)
    upper_case = upper_case_name(name)

    print(f"The length is {length} and the uppercase version is: {upper_case}")
```

Imports

  To import a package from the  standard library, just use: `import package_name`

  Best practice to import modules specifically and not to use " * ", this way you know exactly where a function came from

  Only import what you need, NOT the whole kitchen sink

  ```python
    `from my_module_functions import add_numbers`
  ```

  Use an Alias to reduce verbosity:

  ```python
  import my_math_functions as mmf
  mmf.add_numbers(1, 2)
  ```

## Exceptions

Use `try` and `except` blocks
To catch the value of the exception, use `as`.

```python
try:
  int('a') # will throw an error
except ValueError as error:
  print(f"someting went wrong, {error}")
```

With __Tracebacks__, read them from the bottom to the top

## Context Managers

Open files in the context of `with`, this automatically will close an open file to safely manage resources.

  ```python
  with open("cities.json") as cities_file:
      cities_data = json.load(cities_file)
      ...
      ...
  ```

Methods for context managers are: `open` (opens a file). There are options to pass to enable writing to the file, appending, etc.
READ more about this topic.


## Install packages

`python -m pip install requests` - uses pip as the package manager to install the requests library into the module.
...then at the top of the file `import requests` (this lib makes easy work of retrieving data from API's)

## Object Oriented Programming in Python

`self` is used inside Classes to refer to an instance of the class, not the class itself
self will tell the interpreter to look for an instance variable (runs) in the instance my_car
self is passed as an argument to the class methods

```python
class Car:
    runs = True

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
print(f"My car runs: {my_car.runs}")
my_car.start()
```

If we want a class to have variables available to all instances, they are declared like "runs" above.
`@classmethod` - is a "decorator" written above all the methods that are available to all instances. In these methods, __we do not pass `self`, we pass another variable, `cls`

These methods can be overwrite some of the variables declared

```python

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels
```

`isinstance()` - informs the user if an instance belongs to a particular class.
`issubclass()` - shows if the subclass is in fact derived from a parent class.

Magic Methods

  "Magic Methods" are signified with a double underscore.

  `__init__` - will run whenever a new instance of the class is initiated, we pass "self" and any variable that we want to set when we initiate an new instance

```python
    def __init__(self, make, model):
        self.make = make
        self.model = model
```

`super().` is called before "__init__" `super().__init__(...)` which resolves to our parent class

## Traceback and Exceptions

Always handle errors and catch exceptions:
[Read and Research More about Error Handling](https://practical.learnpython.dev/06_object_oriented_python/50_exceptions/)

Errors during parsing are `SyntaxErrors`

An unhandled exception is called a `Traceback`

Best practice is the catch more specific exceptions first
  Don't catch `Exception`! Way too general
  Especially dont catch `BaseException`!! You'll swallow every single type of exceptipn and you won't even be able to ctl-C and exit the program.

### FEM Python Fundamentals 10/31/24

To start the blog project

1. $ mkdir python_fundamentals
2. $ cd python_fundamentals
3. $ git clone (project repo url)
4. $ cd practical_blog
5. $ create a virtual environment
6. $ python3 -m venv env
7. $ source env/bin/activate
8. $ python3 -m pip install -r requirements.txt
9. $ python3 -m install python3.12.1-distutils
  in python 3 distutils was deprecated, the above command fixes django errors
10. $ python3 manage.py migrate
11. $ python3 manage.py runserver
