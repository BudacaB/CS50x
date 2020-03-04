#include <stdio.h>

int get_int(void);

int main(void) {
    int n;
    do
    {
        n = get_int();
    }
    while (n < 1);
    for (int i = 0; i < n ; i++) {
        printf("?");
    }
    printf("\n");
}

int get_int(void) {
    int n;
    printf("Width: ");
    scanf("%i", &n);
    return n;
}