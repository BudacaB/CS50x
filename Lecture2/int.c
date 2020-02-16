#include <stdio.h>

int main(void)
{
    int age;
    printf("What is your age?\n");
    scanf("%i", &age);
    printf("You are at least %i days old\n", age * 365);
}