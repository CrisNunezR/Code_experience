#include <stdio.h>

int main(void)
{
    int counter =0;
    counter = counter+1;
    printf("counter: %d\n", counter);

    counter += 1;
    printf("counter: %d\n", counter);

    counter++;
    printf("counter: %d\n", counter);

    counter=counter-1;
    printf("counter: %d\n", counter);

    counter -= 1;
    printf("counter: %d\n", counter);

    counter--;
    printf("counter: %d\n", counter);

}