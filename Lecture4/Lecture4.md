## Memory

- binary: 0 1
- decimal: 0 1 2 3 4 5 6 7 8 9
- hexadecimal (hex = 16): 0 1 2 3 4 5 6 7 8 9 A B C D E F -> F is 15

---

Binary - can go highest to 255

128 64 32 16 8 4 2 0 

2<sup>7</sup> 2<sup>6</sup> 2<sup>5</sup> 2<sup>4</sup> 2<sup>3</sup> 2<sup>2</sup> 2<sup>1</sup> 2<sup>0</sup>

0 - 0 - 0 - 0 - 0 - 0 - 0 - 0

1 - 1 - 1 - 1 - 1 - 1 - 1 - 1 => 255

---
Hexadecimal

16 1 

16<sup>1</sup> 16<sup>0</sup>

F - F

0 - 0

- e.g.  0 F => 15 ; 1 0 => 16 (this is not ten as in decimal, in dexadecimal it is one zero) ; 1 F => 31

- F F => 255
- RGB is hexadecilam, e.g. 0 0 0 0 0 0 ; F F 0 0 0 0 => a lot of red, no green, no blue ; F F F F F F => white

Hexadecimal makes mapping easy because a group of 4 binary digits (bits) has 16 different combinations, and each of those combinations maps to a single hexadecimal digit

e.g.

Decimal  Binary  Hexadecimal

...

0 ---------- 0110 - 0x6

15 --------- 1111 - 0xF

- Just like binary has place values - powers of 2 (1, 2, 4, 8 ...) and decimal does too - powers of 10 (1, 10, 100, 1000, ...), so does hexadecimal - powers of 16

    16<sup>2</sup> 16<sup>1</sup> 16<sup>0</sup>

    256 16 1

    0x  3   9  7

    0x  A   D  C

    To convert a binary number into hexadecimal, group 4 binary digits (bits) together from right to left; pad the leftmost group with extra 0 bits at the front if necessary

---

#### Convention

If we have a hexadecimal value, it is prefixed with '0x'

Memory addresses use this convetion -> 0x0 0x1 ... 0x1F etc.

---

& - AddressOf operator (what's the address?)

\* - operator for 'go to the address' - dereference operator

---

#### Strings

String = char array -> a 4 char string for example stores 5 values in 5 sequential bytes - the 4 chars and the termination signal

E ------ M ------ M ------ A ------ \0

0x123 0x124 0x125 0x126 0x127

A string is actually <em>a pointer</em> to the first character - for example string s or char[] s actually stores 0x123, the pointer to the first character's address. 

The PC knows where the string ends with the help of the null terminating character (a byte of eight 0 bits).

```
string s = "EMMA"; == char *s = "EMMA";
```

- for e.g. to create a 'string' datatype, we could do:

 ```
 typedef char *string;
 ```

 ---

 ```
 void swap(int a, int b)
 {
     int tmp = a;
     a = b;
     b = tmp;
 }

```

---

#### Memory allocation:

machine code

globals

heap (this is where malloc takes memory from)

  v

<br>
<br>

  ^
  
stack (this is where variables are stored when functions are called)

When they collide (buffer overflows):
- heap overflow
- stack overflow

<br>

#### C Program (memorcy.c)


swap (storing a, b and tmp)

main (stack frame for argv, argc, x, y)


When swap() is done, the operation is complete, a and b have been swapped, but the stack frame is remove and x and y remain unchanged in the main() stack frame

We can use the pointers and directly changed the variables at their location

```
int tmp = *a;
*a = *b;
b* = tmp;
```

---

#### Pointers

- Pointers are just addresses of locations in memory

- Pointers are useful for passing data / passing data between function

  - we can pass data by value  - we only pass a copy of that data
  - using pointers we can pass the actual variable itself -> a change in one function can impact what happens in a different function

Data types:
- int - 4 bytes
- char - 1 byte
- float - 4 bytes
- double - 8 bytes
- long long - 8 bytes
- char* or for any datatype - 4 or 8 (depending on the system architecture)

```
int k;
k = 5;
int *pk; // point to an int
pk = &k; // this is the int address to point to
```

- A pointer is a data item whose:
  - value is a memory address
  - type describes the data located at that memory address

- Pointers allows data structures and/or variables to be shared among functions

- Pointers make a computer environment more like the real world

- The simplest pointer available in C is the NULL pointer - points to nothing
  - when you create a pointer and you don't set its value immediately, you should always set the value of the pointer to NULL
  - you can check wheter a pointer is NULL using the equality operation (==)

- Another easy way to createa a pointer is to simply extract the address of an already existing variable. We can do this with the address extraction operatpr (&)
  - if x is an int-type variable, then &x is a pointer-to-int whose value is the address of x
  - if arr is an array of doubles, then &arr[i] is a pointer-to-double whose value is the address of the i<sup>th</sup> element of arr -> an array's name then, is actually just a pointer to its first element

- The main purpose of a pointer is to allow us to modify or inspect the location to which it points - we do this by <em>dereferencing</em> the pointer
  - if we have a pointer-to-char called pc, then *pc is the data that lives at the memory address stored inside the pc variable
  - if you try to dereference a pointer whose value is NULL -> segmentation fault (good behavior)

- To create multiple pointers on the same line, each needs the '*' e.g. int *pa, *pb;


