## Python

```
print("hello, world)
```

```
answer = input("What's your name?\n")
print("hello, " + answer)
print("hello,", answer)
print(f"hello, {answer}")
```

```
counter = 0
counter += 1
```

```
if x < y
    print("x is less than y")
elif x > y
    print("x is greater than y")
else
    print("x is equal to y")
```

```
while True:
    print("hello, world")
```

```
i = 3
while i > 0:
    print("cough")
    i -= 1

for i in [0, 1, 2]:
    print("cough")

for i in range(3):
    print("cough")
```

- syntax is simpler tha C
- fewer data types than C
- C data types:
    - bool
    - char
    - double
    - float
    - int
    - long
- python data types:
    - bool
    - float
    - int
    - str
- more powerful data types from python:
    - range - sequence of numbers
    - list - sequence of mutable values (similar to array in C but more flexible)
    - tuple - sequence of immutable values
    - dict - collection of key/value pairs (abstraction of the C hash table)
    - set - collection of unique values

---

#### Regular Expressions

- . any character
- .* 0 or more characters
- .+ one or more characters
- ? optional
- ^ start of input
- $ end of input

---
---

- Python is an example of a very commonly-used modern programming language
    - C was first release in 1972, Python in 1991
- Python is an excellent and versatile language choice for making complex C operations much simpler
    - string manipulation
    - networking
- Fortunately, Python is heavily inspired by C (its primary interpreter, Cpython, is actually written in C) and so the syntax should be a shallow learning curve

---

#### Lists

```
# different ways to create a list
nums = []
nums = [1, 2, 3, 4]
numas = [x for x in range(500)]
nums = list()

nums = [1, 2, 3, 4]
nums.append(5) # adds 5 at the end of the list
nums.insert(4, 5) # adds 5 in the 4th position

nums = [1, 2, 3, 4]
nums[len(nums):] = [5] # create a new list and splice it to the existing one
```
---

#### Tuples

- Python also has a data type that is not quite like anything comparable to C, a **tuple**
- Tuples are ordered, immutable sets of data; they are great for associating collections of data, sort of like a struct in C, but where those values are unlikely to change

```
# a list of four tuples:
presidents = [
    ("George Washington", 1789),
    ("John Adams", 1797),
    ("Thomas Jefferson", 1801),
    ("James Madison", 1809)
]

# this list is iterable as well
for prez, year in presidents:
    print("In {1}, {0} took office".format(prez, year))
```
---

#### Dictionaries

- Python also has built in support for dictionaries, allowing you to specify list indices with words of phrases (**keys**), instead of integers, which you were restricted to in C

```
pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetable": 11,
    "buffalo chicken": 12
}

pizzas["cheese"] = 8

if pizzas["vegetables"] < 12:
    # do something

pizzas["bacon"] = 14
```

- But this create a somewhat new problem... how do we iterate through a dictionary? We don't have indexes randing from [0, n-1] anymore -> the for loop in Python is extremely flexible

```
# transform the dictionary into a list to iterate over it

for pie in pizzas:
    # use pie in here as a stand-in for i
    print(pie)

for pie, price in pizzas.items():
    print(price)

# when transforming into a list the order is not guaranteed

for pie, price in pizzas.items():
    print("A whole {} pizza costs ${}".format(pie, price))
    print("A whole " + pie + " pizza costs $" + str(price))
```
---

#### Functions

- Python has support for functions as well. Like variables, we don't need to specify the return type of the function (because it doesn't matter), nor the data types of any parameters (ditto)
- All functions are introduced with the 'def' keyword
    - also no need for main; the interpreter reads from top to bottom
    - if you with to define main nonetheless (and you might want to), you must at the very end of your code have:

    ```
    if __name__ == "__main__":
        main()
    ```

```
def square(x):
  # return x * x
  return x ** 2
```

---

#### Objects

- Python is an OOP (object-oriented programming) language
- An object is sort of analogous to a C structure
- C structures contain a number of fields, which we might also call properties
    - but the properties themselves can not ever stand on their own

```
# in C
struct car
{
    int year;
    char *model;
}

struct car herbie;
herbie.year = 1963;
herbie.model = "Beetle";
```

- Objects, meanwhile, have properties but also **methods**, or functions that are inherent to the object, and mean nothing outside of it. You define the methods inside the objects also
    - thus, propertis and methods don't ever stand on their own
- object.mehod() - calling the method of an object
- You define a type of object using the **class** keyword in Python
- Classes require an initialization function, also more generally known as a **constructor**, which sets the starting values of the properties of the object
- in defining each method of an object, **self** should be its first parameter, which stipulates on what object the method is called

```
class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def changeID(self, id):
        self.id = id
    
    def print(self):
        print("{} - {}".format(self.name, self.id))

jane = Student("Jane", 10)
jane.print()
jane.changeID(11)
jane.print()
```

---

#### Style

- Good style is crucial in Python
- Tabs and indentation actually matter in this language, and things will not work the way you intend for them to if you disregard styling

- Python programs can be prewritten in .py files, but you can also write and test short Python snippets using the Python interpreter from the command line
- You can also make your programs look a lot more like C programs when they execute by adding a **shebang** to the top of the Python files, which automatically finds and executes the interpreter

```
#!/usr/bin/env python3
```
- If you do this, you need to change the permissions on the file using 'chmox +x \<file>' and the launching it with './\<file>'