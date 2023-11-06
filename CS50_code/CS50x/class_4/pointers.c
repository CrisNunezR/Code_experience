#include <stdio.h>
//#include <cs50.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    //printf("%p\n", p);
    //printf("%i\n", *p);

    //we can also use strings as a pointer to the 1st char of the string
    char *s = "Hi!";

    printf("%c\n", *s);
    printf("%s\n", (s+500000));
    printf("%c\n", s[2]);

}
