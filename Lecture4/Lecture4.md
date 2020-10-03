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

---

#### Dynamic memory allocation

- We can use pointers to get access to a block of dynamically-allocated memory at runtime
- Dynamically allocated memory comes from a pool of memory known as the heap
- Prior to this point, all memory we've been working with has been coming from a pool of memory known as the stack
- Usually true:
  - a variable that's given a name, probably lives on the stack
  - a variable not given a name (with dynamic memory allocation), lives on the heap
- We get this dymanically-allocated memory by making a call to the C standard library function malloc(), passing as its parameter the number of bytes requested
  - after obtaining memory (if it can), malloc() will return a pointer to that memory
  - if malloc() can't get memory, it will return NULL (it's best to check for this before dereferencing to avoid the segmentation fault error)


```
// statically obtain an integer
int x;

// dynamicaly obtain an integers
int *px = malloc(sizeof(int));
```

```
// get an integer from the user
int i;
printf("i: ");
scanf("%d", &i);

// array of floats on the stack
float stack_array[x];

// array of floats on the heap
float* heap_array = malloc(x * sizeof(float));
```

- Here's the trouble: dynamically-allocated memory is not automatically returned to the system for later use when the function in which it's created finishes execution
  - failing to return memory back to the system when you're finished with it results in a memory leak which can compromise your system's performance
  - when you finish working with dynamically-allocated memory, you must free() it

```
char* word = malloc(50 * sizeof(char));

// do stuff with word

// now we're done working with that block
free(word);
```

- Three golden rules:
  1. every block of memory that you malloc() must subsequently be free()d
  2. Only momery that you malloc() should be free()d
  3. Do not free() a block of memory more than once

```
int m; // create an int variable on the stack, called m (a box capable of holding an integer)

int* a; // create a box on the stack, called a (capable oh holding int* - pointers to integers)

int* b = malloc(sizeof(int)); // creates two boxes (one on the heap - unnamed, and b on the stack) and establishes a pointer relationship, from b to the other box -> basically a piece of memory, b that points (contains the address) to another piece of memory

a = &m; // a gets m's address (a now points to m)

a = b; // a now points to the same place that b points to (inside of a is now the same address that is inside b)

m = 10; // put a 10 in the m box

*b = m + 2; // dereference b and put a value, m + 2 (12), in that memory location

free(b); // give up the memory and empty the box that b points to

*a = 11; // segmentation fault - now we longer have access to that piece of memory
```

---

#### Call stacks

- When you call a function, the system sets aside space in memory for that function to do its necessary work.
  - we frequently call such chunks of memory <em>stack frames</em> or <em>function frames</em>

- More than one function's stack frame may exist in memory at a given time. If main() calls move(), which then calls direction(), all three functions have open frames, but only one is active at any given time

- These frames are arranged in a <em>stack</em>. The frame for the most recently function is always on the top of the stack

- When a new function is called, a new frame is <em>pushed</em> onto the top of the stack and becomes the active frame

- When a function finishes its work, its frame is <em>popped</em> off the stack, and the frame immediately below it becomes the new, active, function on the top of the stack. This function picks up immediately where it left off

```
int fact(int n)
{
  if (n == 1) 
    return 1;
  else
    return n * fact(n - 1);
}

int main(void)
{
  printf("%i\n", fact(5));
}
```

fact(1)

fact(2)

fact(3)

fact(4)

fact(5)

printf()

main()

---

#### File pointers

- The ability to read data from and write data to files is the primary means of storing persistent data, data that does not disappear whrn your program stops running

- The abstraction of files that C provides is implemented in a data structure known as a FILE
  - almost universally when working with files, we will be using pointers to them, FILE*

- The file manipulation functions all live in stdio.h
  - all of them accept FILE* as one of their parameters, except for the function fopen(), which is used to get a file pointer in the first place

- Some of the most common file input/output (I/O) functions that we'll be working with are: fopen(), fclose(), fgetc(), fputc(), fread(), fwrite()

- fopen()
  - opens a file and returns a file pointer to it
  - always check the return value to make sure that you don't get back NULL

  ```
  FILE* ptr = fopen(<filename>, <operation>);
  ```

- fclose()
  - closes the file pointed to by the given file pointer

  ```
  fclose(<file pointer>);
  ```

- fgetc()
  - reads and returns the next character from the file pointed to
  - Note: the operation of the file pointer passed in as a parameter must be "r" for read, or you will suffer an error

  ```
  char ch = fgetc(<file pointer>);
  ```

  - The ability to get single characters from files, if wrapped in a loop, means we could read all the characters from a file and print them to the screen, one by one, esentially

  ```
  char ch;
  while((ch = fget(ptr)) != EOF)
    printf("%c", ch);
  ```

- We might put this in a file called cat.c, after the Linux command cat which essentially does just this

- fputc()
  - writes or appends the specified character to the pointed-to file
  - Note: the operation of the file pointer passed in as a parameter must be "w" for write or "a" for append, or you will suffer an error

  ```
  fputc(<character>, <file pointer>);
  ```

  - Now we can read characters from files and write characters to them. Let's extend our previous example to copy one file to another, instead of printing to the screen
  
  ```
  char ch;
  while((ch = fgetc(ptr)) != EOF)
    fputc(ch, ptr2);
  ```

  - we might put this in a file called cp.c, after the Linux command "cp" which essentially does just this

- fread()
  - reads \<qty> units of size \<size> from the file pointed to and stores them in memory in a buffer (usually an array) pointed to by \<buffer>
  - Note: the operation of the file pointer passed in as a parameter must be "r" for read, or you will suffer an error

  ```
  fread(<buffer>, <size>, <qty>, <file pointer>)
  ;

  int arr[10]; // on the stack
  fread(arr, sizeof(int), 10, ptr) // we're reading sizeof(int) * 10 bytes of info (40 bytes) from the file pointer to by ptr and we're storing them in arr
  ```

  - we can also dynamically allocate a buffer
  ```
  double* arr2 = malloc(sizeof(double) * 80); // on the heap
  fread(arr2, sizeof(double), 80, ptr);
  ```

  - we can also use fread() just a call to fgetc() and get one character - we don't need an array -> the catch is that if we have a variable, we need to pass in the address of that variable, because the buffer is a pointer to the location in memory where we want to store the info

  ```
  char c;
  fread(&c, sizeof(char), 1, ptr);
  ```

- fwrite()
  - writes \<qty> units of size \<size> to the file pointed to by reading them from a buffer (usually an array) pointed to by \<buffer>
  - Note: the operation of the file pointer passed in as a parameter must be "w" or "a", or you will suffer an error

  ```
  fwrite(<buffer>, <size>, <qty>, <file pointer>);

  int arr[10];
  fwrite(arr, sizeof(int), 10, ptr);
  ```
   - we can also dynamically allocate a buffer
  ```
  double* arr2 = malloc(sizeof(double) * 80); // on the heap
  fwrite(arr2, sizeof(double), 80, ptr);
  ```

- Other useful functions from stdio.h
  - fgets() - reads a full string from a file
  - fputs() - write a full string to a file
  - fprintf() - writes a formatted string to a file
  - fseek() - allows you rewind or fast-forward within a file
  - ftell() - tells you at what (byte) position you are within a file
  - feof() - tells you whether you've read to the end of a file
  - ferror() - indicates whether an error has occurred in working with a file
