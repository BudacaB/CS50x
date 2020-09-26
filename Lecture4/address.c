#include <stdio.h>

int main(void)
{
    int n = 50;
    // printf("%i\n", n);
    // printf("%p\n", &n); // p = pointer
    // printf("%i\n", *&n);

    int *p = &n; // this says that 'p' is a pointer, and 'int' signals that it points to an int
    printf("%p\n", p);
    printf("%i\n", *p);
}