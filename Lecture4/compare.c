#include <stdio.h>

int main(void)
{
    // int i, j;
    // printf("i: ");
    // scanf("%d", &i);
    // printf("j: ");
    // scanf("%d", &j);

    // if (i == j) 
    // {
    //     printf("Same\n");
    // }
    // else
    // {
    //     printf("Different\n");
    // }
    
    char s[20], t[20];
    printf("s: ");
    scanf("%s", s);
    printf("t: ");
    scanf("%s", t);

    printf("%p\n", s);
    printf("%p\n", t);
}