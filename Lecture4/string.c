#include <stdio.h>

int main(void)
{
    char *s = "EMMA";
    printf("%s\n", s); // %s tells the compiler to print all the chars until it meets the null character
    printf("%p\n", s);
    printf("%c\n", *s);
    printf("%c\n", s[1]);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    printf("%p\n", &s[4]);
    printf("%i\n", s[4]);

    // [] is syntactic sugar, the compiler actually does this
    printf("%c\n", *s);
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
    printf("%c\n", *(s+3));
}