#include <stdio.h>
#include <string.h>

int main(void)
{
    FILE *file = fopen("phonebook.csv", "a"); // a = append

    // Get strings from user
    char name[15];
    char number[15];
    printf("Name: ");
    scanf("%s", name);
    printf("Number: ");
    scanf("%s", number);

    // Print (write) strings to file
    fprintf(file, "%s,%s\n", name, number);

    // Close file
    fclose(file);
}