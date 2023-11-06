#include <cs50.h>
#include <stdio.h>
#include <math.h>
// this function tests for prime numebers within a range
// the prime subfunction returns TRUE if it is a prime number and FALSE if it isnt

bool prime(int number);

int main(void)
{
    int min;
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);

    int max;
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);

    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
    //divide "number" by every intenger bt 2 and sqrt("number")+1
    //if remainder is > 0 for all, the number is prime

    // TODO
    bool prime = true;
    //considers 1 and 2
    switch (number)
    {
        case 1:
            prime = false;
            break;
        case 2:
            prime = true;
            break;
        case 3:
            prime = true;
            break;
        default:
            for (int i = 2; i < number - 1; i++)
            {
                if (number % i == 0)
                {
                    //printf("%i / %i\n", number, i);
                    prime = false;
                    break;
                }
            }
    }
    return prime;
}