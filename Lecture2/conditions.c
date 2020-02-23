// Conditions and relational operators

#include <stdio.h>

int main(void) {

    // Prompt user for x
    int x;
    printf("x: ");
    scanf("%i", &x);

    // Prompt user for y
    int y;
    printf("y: ");
    scanf("%i", &y);

    // Compare x and y
    if (x < y) {
        printf("x is less than y\n");
    }
    else if (x > y) {
        printf("x is greater than y\n");
    }
    else {
        printf("x is equal to y\n");
    }
}