#include <cs50.h>
#include <stdio.h>

void set_array(int array[3]);
void set_int(int x);

int main(void)
{
    int a = 10;
    int b[3] = {0,2,3};

    set_int(a);

    set_array(b);

    printf("%p %d\n", &a, b[0]);
}

void set_array(int array[3])
{
    array[0] = 5;
}

void set_int(int x)
{
    x = 3*x;
}