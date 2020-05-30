#include <stdio.h>

// const int N = 3;

float average(int length, int array[]);

int main(void)
{
    // int scores[N];
    // scores[0] = 72;
    // scores[1] = 73;
    // scores[2] = 33;
    // int scores[3] = {72, 73, 33};
    // int scores[] = {72, 73, 33};

    int n;
    printf("Number of scores: ");
    scanf("%i", &n);

    int scores[n];

    for (int i =0; i < n; i++)
    {
        printf("Score %i: ", i + 1);
        scanf("%i", &scores[i]);
    }

    printf("Average is %.1f\n", average(n, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return (float) sum / (float) length;
}