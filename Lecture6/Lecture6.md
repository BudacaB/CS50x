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