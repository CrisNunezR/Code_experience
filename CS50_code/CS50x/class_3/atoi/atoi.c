#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);      //recursive version
int convert_loop(string input); //loop version
string trim_string(string to_trim);

int main(void)
{
    string input = get_string("Enter a positive integer: ");
    int ret_value;

    //validates that all elements of the string are digits before calling the convertion function
    //is this efficient, though? 'cause this is basically converting to validate, right?
    int n = strlen(input);
    for (int i = 0; i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    //imprime texto
    //printf("Nro en texto: %s\nNro por caracter:", input);

    //for (int j = 0; j < n; j++)
    //{
    //    printf("%c", input[j]);
    //}
    //input[n-1] = input[n];

    //printf("\n");
    //printf("texto ajuste NULL: %s\n. Strlen texto ajustado: %i\n", input, (int) strlen(input));

    // Convert string to int
    ret_value = convert(input);
    //printf("number is: %i\nand multiplied by 2: %i\n", ret_value, ret_value * 2);
    printf("%i\n", ret_value);
}

//function to convert strings into integers
//loop implementation
int convert_loop(string input)
{
    int ret_value = 0;
    int str_len = strlen(input);
    for (int i=0; i < str_len; i++)
    {
        //printf("%i", (input[i] - 48) * pow(10, str_len - (i+1));
        ret_value = ret_value + (input[i] - 48) * pow(10, str_len - (i+1)); //stores the value of the digit value multiplied by the corresponding base-10
    }
    return ret_value;
}

//function to convert strings into integers
//recursive implementation
int convert(string input)
{
    // TODO -- recursive section
    if (strlen(input) >  1)
    {
        //takes last value of received string and calculates its integer value
        //then recursively call convert multiplying by 10 to account for the increase in position
        //notice the substraction of ASCII value 48, since 0 == 48 in ASCII
        int i = input[strlen(input) - 1] - 48;
        return (10 * convert(trim_string(input)) + i);      //recursive call
    }
    else
    {
        return (int) input[0] - 48;
    }
}

//function that returns a given string array without its last element
//by swapping the '/0' element with the final actual 'string' element of the array
string trim_string(string to_trim)
{
    //identifies length of string (up to right before the /0 == NULL element of the array)
    int str_len = strlen(to_trim);

    //swapps the last 2 elements, thus truncating the string
    to_trim[str_len - 1] = to_trim[str_len];

    return to_trim;
}