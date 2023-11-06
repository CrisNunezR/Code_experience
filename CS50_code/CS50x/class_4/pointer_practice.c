#include <stdio.h>
#include <cs50.h>


int main(void)
{
    int a = 28; //this assigns 28 to a at an undefined memory space
    int b = 50; //this assigns 50 to b at an undefined memory space
    int *c = &a; //this assigns the address of the memory space where 'a' is located to 'c'

    *c = 14;    //this defines the address stored at c as 14
    c = &b;     //this stores the address where 'b' is stored as a value to c
    *c = 25;    // this defines the address stored at c as 14

    //print the results

    // this should be 14 since *c=14 assigned 14 to the address assigned for *c, which is &a
    //where the value for a is stored
    printf("a has the value %i, located at %p\n", a, &a);

    //this should be 25, since c=&b did the same thing
    printf("b has the value %i, located at %p\n", b, &b);

    //this should return the value for *c (which is the location of &b) and its location, which can be anythingcd
    
    printf("c has the value %p, located at %p\n", c, &c);
}