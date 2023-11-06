#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

float calc_hours(int hours[], int weeks, char output);

int main(void)
{
    int weeks = get_int("Number of weeks taking CS50: ");
    int hours[weeks];

    for (int i = 0; i < weeks; i++)
    {
        hours[i] = get_int("Week %i HW Hours: ", i);
    }

    char output;
    do
    {
        output = toupper(get_char("Enter T for total hours, A for average hours per week: "));
    }
    while (output != 'T' && output != 'A');

    printf("%.1f hours\n", calc_hours(hours, weeks, output));
}

// TODO: complete the calc_hours function
float calc_hours(int hours[], int weeks, char output)
{
    float sum_hours = 0;
    int counter;

    //calculates the total number of hours in the weeks passed
    for (counter = 0; counter < weeks; counter++)
    {
        sum_hours = sum_hours + hours[counter];
    }

    //determines whether to calculate average or just deliver the sum
    //we will assume we will only receive A (ASCII 65)and T(ASCII 84) as variables
    if (output == 65)
    {
        //output => average
        return ((float) sum_hours / weeks);
    }
    else if (output == 84)
    {
        return sum_hours;
    }

    return 0.0;
}