#include <stdio.h>

int main(void)
{
    float price;
    printf("What is the price?\n");
    scanf("%f", &price);
    //printf("Your total is %f\n", price * 1.0625);
    printf("Your total is %.2f\n", price * 1.0625);
}