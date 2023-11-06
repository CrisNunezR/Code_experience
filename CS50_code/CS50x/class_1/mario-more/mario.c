#include <cs50.h>
#include <stdio.h>

void print_space_n(int n);
void print_hash_n(int n);

//function creates 2 towers with a user-given number of storeys
int main(void)
{
    //Receives height of the tower
    int height;
    do
    {
        height = get_int("Please enter a positive integer smaller than 9: ");
    }
    while (height > 8 || height < 1);

    //draws tower
    //first, define the number of levels
    for (int level = 0; level < height; level++)
    {
        //now, print spaces for each level for the left side
        print_space_n(height - level);

        //now, print the # for the left side
        print_hash_n(level);

        //now print 2 spaces to separate the towers
        printf("  ");

        //now, print the # for the right side
        print_hash_n(level);

        //now that we have both sides, continue to the next level
        printf("\n");
    }
}

//function that prints n-1 consecutive spaces
void print_space_n(int n)
{
    for (int i = 1; i < n ; i++)
    {
        printf(" ");
    }
}

//function that prints n+1 hash-tags #
void print_hash_n(int n)
{
    for (int i = 0; i < n + 1 ; i++)
    {
        printf("#");
    }
}