#include <stdio.h>
#include <cs50.h>

int main(void)
{


    //checking using the string format
    string s = "HI!";
    printf("%s\n", s);
    printf("%i %i %i %i \n", s[0], s[1], s[2],s[3]);
    printf("%c%c%c%c \n", s[0], s[1], s[2], s[3]);

    int i = s[0];
    printf("this is the ASSCI dec value of 'H': %i\n", s[0]);

    //but we can also print the values
    //that the computer uses to represent earh char
    //printf("%i %i %i \n", c1, c2, c3);

    //create a string with characters
    //char c1 = 'H';
    //char c2 = 'I';
    //char c3 = '!';

    //note that we can print the string:
    //printf("%c%c%c \n", c1, c2, c3);


    //create an array of 3 values
    //int values_1[3] = {30,20,4};
    //printf("values_1[1]: %i\n",values_1[1]);

    //alternatively, we can do ir value by value
    //int values_2[3];

    //values_2[0]=30;
    //values_2[1]=20;
    //values_2[2]=4;

    //printf("values_2[1]: %i\n",values_2[1]);
}