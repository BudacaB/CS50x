#include <stdio.h>
#include <string.h>

typedef struct
{
    char name[50];
    char number[50];
}
person;

int main(void)
{
    // char *names[4] = { "Emma", "Rob", "Doug", "Brian" };
    // char *numbers[4] = { "0723-343-565", "0725-222-513", "0721-678-345", "0722-898-123" };

    person people[4];

    strcpy(people[0].name, "Emma");
    strcpy(people[0].number, "0723-343-565");

    strcpy(people[1].name, "Rob");
    strcpy(people[1].number, "0725-222-513");

    strcpy(people[2].name, "Doug");
    strcpy(people[2].number, "0721-678-345");

    strcpy(people[3].name, "Brian");
    strcpy(people[3].number, "0722-898-123");

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, "Emma") == 0)
        {
            printf("%s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found");
    return 1;
}