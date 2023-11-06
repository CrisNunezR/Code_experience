// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol!\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    //there are basically 2 ways to implement this
    //one is to directly use the actual dec values for the ASCCI chars
    //the other is to use the c.type.h library

    //eather way, we'll need 4 boolean variables to validate
    //we'll initialize all of them to false
    bool upper = false;
    bool lower = false;
    bool number = false;
    bool symbol = false;

    //1st let's try using the actual values

    //we'll need to go through the string and check each character
    //we'll use a while loop to check each char until we find and NULL/end_of_string
    //note that we define c_dec as an integer to get the decimal/ASCII value
    int c_dec;

    int i = 0;
    while (password[i] != 0)
    {
        c_dec = password[i];

        //now, we chech each char
        if (c_dec >= 65 && c_dec <= 90)
        {
            upper = true;
        }
        else if (c_dec >= 97 && c_dec <= 122)
        {
            lower = true;
        }
        else if (c_dec >= 48 && c_dec <= 57)
        {
            number = true;
        }
        else if (c_dec >= 33 && c_dec <= 47)
        {
            symbol = true;
        }

        i++;
    }

    //now we check if all the requirements are met
    if( upper && lower && number && symbol)
    {
        return true;
    }
    else
    {
        return false;
    }

}
