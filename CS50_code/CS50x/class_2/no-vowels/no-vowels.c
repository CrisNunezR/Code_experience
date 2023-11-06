// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>

char convert_vowel(char x);
bool is_vowel(char x);
int get_str_size(string str);

int main(int argc, string argv[])
{
    //checks whether only one string was entered
    if ((argc == 1) || (argc > 2))
    {
        printf("Please enter just one string to convert.\n");
        return 1;
    }
    else
    {
        //identifies the lenght of the string
        int str_size = get_str_size( argv[1] );

        //defines variables to store the converted string
        //(notice that it must be defined as char not strings=> it's the type of the inner elements of the array!!!
        //also, we need to define the size + 1 to account for the 'NULL' character that defines the end of the string
        char str_convert[str_size+1];

        //assigns the string to a dummy string variable
        string str_vowels = argv[1];

        //printf("%s\n", str_vowels);
        //for (int i = 0; i < str_size; i++)
        //{
        //    printf("%c\n", str_vowels[i]);
        //}

        //checks letter by letter to define whether to convert and convert if it applies
        for (int i = 0; i < str_size; i++)
        {
            if (is_vowel( (char) str_vowels[i] ) )
            {
                //is_vowel returned 'true' so it is a vowel to convert
                str_convert[i] = (char) convert_vowel((char) str_vowels[i]);
            }
            else
            {
                // is_vowel returned 'flase' so no need to convert
                str_convert[i] = (char) str_vowels[i];
            }
        }

        //now we need to 'close' the string to avoid strange characters appearing
        str_convert[str_size] = 0;

        printf("%s is turned to %s\n", str_vowels, str_convert);
    }
}


//function that identifies the size of a string
int get_str_size(string str)
{
    int i=0;
    while ( str[i] != 0 )
    {
        i++;
    }
    return i;
}

//function to convert vowels according to the definition
char convert_vowel(char x)
{
    switch ( x )
    {
        case 'a':
            return '6';
            break;
        case 'A':
            return '6';
            break;

        case 'e':
            return '3';
            break;
        case 'E':
            return '3';
            break;

        case 'i':
            return '1';
            break;
        case 'I':
            return '1';
            break;

        case 'o':
            return '0';
            break;
        case 'O':
            return '0';
            break;

        case 'u':
            return 'u';
            break;
        case 'U':
            return 'U';
            break;
        default:
            return ' ';
    }
}

//function to tell vowels from consonants
bool is_vowel(char x)
{
    switch ( x )
    {
        //checks for lower case
        case 'a':
            return true;
            break;
        case 'e':
            return true;
            break;
        case 'i':
            return true;
            break;
        case 'o':
            return true;
            break;
        case 'u':
            return true;
            break;
        //checks for upper case
        case 'A':
            return true;
            break;
        case 'E':
            return true;
            break;
        case 'I':
            return true;
            break;
        case 'O':
            return true;
            break;
        case 'U':
            return true;
            break;
        default:
            return false;
    }
}