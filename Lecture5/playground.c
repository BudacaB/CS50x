// Implements a spell-checker

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "./dictionary.h"


// Default dictionary
#define DICTIONARY "./dict2"

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
#define N 5000

int words = 0;

// Hash table
node *table[N];

int main(int argc, char *argv[])
{
    bool loaded = load(DICTIONARY);
    printf("%d\n", loaded);

    for (int i = 0; i < N; i ++) {
        if (table[i] != NULL) {
            for (node *tmp = table[i]; tmp != NULL; tmp = tmp->next)
            {
                printf("%i", i);
                printf("%s\n", tmp->word);
            }
        }
    }

    printf("%i words added\n", size());
    bool found;
    found = check("test");
    printf("%d\n", found);
}

bool load(const char *dictionary)
{
    FILE* file;
    file = fopen (dictionary, "r");
    if (file == NULL)
    {
        printf("The file does not exist\n");
        return 1;
    }

    char word_buffer[LENGTH + 1];

    while(1)
    {
        if(fscanf(file, "%s", word_buffer) == EOF)
        {
            return true;
        }
        words++;
        node* n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("No memory\n");
            return 1;
        }
        strcpy(n->word, word_buffer);
        n->next = NULL;

        int index = hash(word_buffer);
        if (table[index] == NULL)
        {
            table[index] = n;
        }
        else
        {
            n->next = table[index];
            table[index] = n;
        }

    }
    return false;
}

unsigned int hash(const char *word)
{
    int total = 0;
    for (int i = 0; i < strlen(word) ; i++)
    {
        total = total + tolower(word[i]);
    }
    return total % N;
}

unsigned int size(void)
{
    return words;
}

bool check(const char *word)
{
    int index = hash(word);
    node *cursor = table[index];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node* tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
        }
    }
    return true;
}
