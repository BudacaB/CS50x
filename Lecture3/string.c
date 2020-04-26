#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[20];
    printf("Input: ");
    scanf("%s", s);
    printf("Output: ");

    // for (int i = 0; s[i] != '\0'; i++)
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}