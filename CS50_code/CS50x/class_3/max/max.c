// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        arr[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(arr, n));
}

// TODO: return the max value
int max(int array[], int n)
{
    int max_ = array[0];    //initialices max value as the 1st element in the array

    //searches for a lower value
    for (int i = 0; i < n; i++)
    {
        if (array[i] > max_)
        {
            max_ = array[i];
        }
    }

    return max_;
}
