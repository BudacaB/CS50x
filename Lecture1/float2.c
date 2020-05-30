#include <stdio.h>

int main(void) {
    float x;
    printf("x: ");
    scanf("%f", &x);

    float y;
    printf("y: ");
    scanf("%f", &y);

    printf("x / y = %.10f\n", x / y);
}