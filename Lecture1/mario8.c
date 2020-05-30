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
        for (int j = 0; j < n; j++) {
            printf("#");
        }
        printf("\n");
    }
    printf("\n");
}

int get_int(void) {
    int n;
    printf("Size: ");
    scanf("%i", &n);
    return n;
}