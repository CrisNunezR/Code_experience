#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // TODO: Prompt for start size
    int strt_pop=0;
    while (strt_pop < 9)
    {
        strt_pop = get_int("Please enter an initial llamas population (must be > 8): ");
    }

    // TODO: Prompt for end size
    int end_pop = 0;
    while (end_pop < strt_pop)
    {
        end_pop = get_int("Please enter the expected final population of llamas (must be > %i): ", strt_pop - 1);
    }

    // TODO: Calculate number of years until we reach threshold
    //We know that N_final / N_initial = (13/12)^x, with x number of years
    //With that, using a "brute force" approach, we can use a counter to evaluate when the population has increased enough through the years
    //notice that we are unsing the pow operation (included in the math library) and that x is the "end of the year"
    // so x=1 means 12 months have passed
    int x = -1;
    do
    {
        x++;
        //printf("Comparing %i and %f, year %i\n", end_pop, strt_pop * pow( (double) 13/12 , x ), x);
    }
    //while (  x<10 );
    while (  end_pop > (double) strt_pop * pow( (double) 13/12, x) );

    // TODO: Print number of years
    printf("Years: %i\n", (int) x);
}
