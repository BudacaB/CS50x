#include <stdio.h>

int main(int argc, char *argv[])
{
    // Ensure user ran program with 2 words at prompt
    if (argc != 2)
    {
        return 1;
    }
 
    // Open file
    FILE *file = fopen(argv[1], "r"); // r = read
    if (file == NULL)
    {
        return 1;
    }

    // Read 3 bytes from file
    char bytes[3];
    fread(bytes, 3, 1, file);

    // Check if bytes are 0xff 0xd8 0xff -> standard for jpg images
    if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff)
    {
        printf("Maybe\n");
    }
    else
    {
        printf("No\n");
    }
}