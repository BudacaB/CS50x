#include <stdio.h>

int get_positive_int(void);

int main(void) {
    int i = get_positive_int();
    printf("%i\n", i);
}

int get_positive_int(void) {
    int n;
    do
    {
        printf("Positive Integer: ");
        scanf("%i", &n);
    } 
    while (n < 1);
    return n;
}