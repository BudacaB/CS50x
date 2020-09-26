#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char *s;
    printf("s: ");
    scanf("%s", s);

    // char *t = s;
    // t[0] = toupper(t[0]);

    // printf("%s\n", s);
    // printf("%s\n", t);

    char *t = malloc(strlen(s) + 1); // allocate memory for a new string

    // for (int i = 0, n = strlen(s); i <= n; i++) {
    //     t[i] = s[i];
    // }

    strcpy(t, s);

    t[0] = toupper(t[0]);
    printf("%s\n", s);
    printf("%s\n", t);
}