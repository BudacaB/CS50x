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

---

#### Convention

If we have a hexadecimal value, it is prefixed with '0x'

Memory addresses use this convetion -> 0x0 0x1 ... 0x1F etc.

---

& - AddressOf operator (what's the address?)

\* - operator for 'go to the address'

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