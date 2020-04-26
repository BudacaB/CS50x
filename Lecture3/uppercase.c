#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char s[20];
    printf("Before: ");
    scanf("%s", s);
    printf("After: ");

    // for (int i = 0, n = strlen(s); i < n; i++)
    // {
    //     if (s[i] >= 'a' && s[i] <= 'z')
    //     {
    //         printf("%c", s[i] - 32);
    //     }
    //     else
    //     {
    //         printf("%c", s[i]);
    //     }
    // }

    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));
    }
    printf("\n");

}