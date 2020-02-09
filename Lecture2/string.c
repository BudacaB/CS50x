#include <stdio.h>
#include <string.h>

int main(void)
{
    char answer[20];
    printf("What's your name?\n");
    scanf("%s", answer);
    printf("Hello %s\n", answer);
}