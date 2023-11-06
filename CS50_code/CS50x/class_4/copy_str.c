#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>

//this code shows the difference caused by the pointer quality of strings
int main(void)
{
    char *s = get_string("s: ");

    //notice that by copying with this method
    //we are assigning to 't' the same reference to the memory location stored in s
    char *t = s;

    //this capitalises the 1st char of the string
    t[0] = toupper(t[0]);

    //notice that, since all we did was assign to 't' the same address value as 's'
    //'t' will point to the same string as 's', so changing 't' will also change 's'
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    //to actually change just one of those strings, we need to assign a different memory space to 't'
    //this is done with the memory allocation instruction 'malloc'...
    //notice that we are requesting + 1 to allow for the /0 null character that ends the string
    //note: malloc requires the library stdlig=b
    printf("\nNew method allocating new memory section\n");
    s = get_string("s: ");
    char *t_ = malloc(strlen(s) + 1);

    //now we copy, char by char, one string onto the other (notice that we use the strlen + 1 to include the /0 char)
    for (int i = 0; i < strlen(s) + 1; i++)
        //there's a more efficient way to code this 'for' that avoids the calculation of strlen everytime the for is run:
        // for (int i = 0, n = strlen(s) + 1; i < n; i++)
    {
        t_[i] = s[i];
    }

    //now we can safely assign
    t_[0] = toupper(t_[0]);

    //and we'll get different strings for 's' and 't'
    printf("s: %s\n", s);
    printf("t: %s\n", t_);

}