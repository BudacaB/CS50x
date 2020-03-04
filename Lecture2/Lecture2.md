### C language

```
#include <stdio.h>

int main(void) {
    printf("hello, world")
}
```

---

```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string(What's your name?\n");
    printf("Hello, %s\n", answer)
}

```

---

```
if (x < y)
{
    printf("x is less than y\n");
}
else if (x > y)
{
    printf ("x is greater than y\n");
}
else
{
    printf("x is equal to y\n");
}
```

---

```
int i = 0;
while (i < 50)
{
    printf("hello, world\n");
    i++;
}
```

---

```
for (int i = 0; i < 50; i++)
{
    printf("hello, world\n");
}
```

---

bool

char

double

float

int

long

string

---

%s - string

%c - char

%f - float, double

%i - int

%li - long

---
while ... do -> checks condition, then executes

do ... while -> executes, then checks condition