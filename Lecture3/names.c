#include <stdio.h>
#include <string.h>

int main(void)
{
    char *names[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};

    printf("%s\n", names[3]);
    printf("%c%c%c%c\n", names[0][0], names[0][1], names[0][2], names[0][3]);
}