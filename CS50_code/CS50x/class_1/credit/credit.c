#include <cs50.h>
#include <stdio.h>
#include <math.h>

bool checksum(long cred_card);
string brand_check(long cred_card);
int get_last_dig(long x);
int sum_digits(int x);
int get_1st_2(long x);

int main(void)
{
    //get card number from user
    long card = 0;
    card = get_long("Please enter card number here: ");
    //card = 371449635398431;
    if (card < 1000000000000)
    {
        printf("INVALID\n");
        card = 0;
    }

    //validate card number assumes "false" by default. If card is valid, check brand
    bool card_valid = false;
    if (card > 0)
    {
        card_valid = checksum(card);

        //if valid card, get brand using function, otherewise print "Invalid"
        if (card_valid == false)
        {
            printf("INVALID\n");
        }
        else
        {
            printf("%s\n", brand_check(card));
        }
    }
}

//function to validate sum
bool checksum(long cred_card)
{
    int odd_dig_record = 0;
    int even_dig_record = 0;
    long card = cred_card;

    //checks digits from card number one by one
    int counter = 1;
    while (card > 0)
    {

        if (counter % 2 == 0)
        {
            //odd digit, multiply by 2 and add
            //printf("remaining card numbers: %li\n", card);
            //printf("odd_register: %i + %i (=sum digits for %i) \n", odd_dig_record, sum_digits(2 * get_last_dig(card)), 2*get_last_dig(card));
            even_dig_record = even_dig_record + sum_digits(2 * get_last_dig(card));

        }
        else
        {
            //even digit, just add the values of the digits
            //printf("remaining card numbers: %li\n", card);
            odd_dig_record = odd_dig_record + get_last_dig(card);
            //printf("even_register: %i = %i + previous\n", even_dig_record, get_last_dig(card));
        }

        //eliminate last digit and repeat, increasing the counter
        counter++;
        card = card / 10;
    }

    //validates card
    //printf("card: %li\n even_register:= %i\n odd_register= %i\n sum=%i\n", cred_card, even_dig_record, odd_dig_record, even_dig_record + odd_dig_record);
    if (get_last_dig(even_dig_record + odd_dig_record) == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

//function that receives a long number and returns its last digit
int get_last_dig(long x)
{
    //returns the last digit of x by using the default truncation of "x / 10"
    //printf("%f and %li\n", (double) x / 10, (long) (x / 10) );
    return (int) round(10 * (((double) x / 10) - (long)(x / 10)));
}

//function sums digits to a number when the number is larger than 10
int sum_digits(int x)
{
    if (x < 10)
    {
        return x;
    }
    else
    {
        return (get_last_dig(x) + get_last_dig(x / 10));
    }
}

//function to validate card brand
string brand_check(long cred_card)
{
    //get 1st 2 digits from card
    int first2 = get_1st_2(cred_card);

    switch (first2)
    {
        case 34:
            return "AMEX";
            break;
        case 37:
            return "AMEX";
            break;
        case 51:
            return "MASTERCARD";
            break;
        case 52:
            return "MASTERCARD";
            break;
        case 53:
            return "MASTERCARD";
            break;
        case 54:
            return "MASTERCARD";
            break;
        case 55:
            return "MASTERCARD";
            break;
        default:
            if (first2 / 10 == 4)
            {
                return "VISA";
            }
            //Notice that if the card number fulfills Luhn's algorithm we should assume we don't know the card's brand, not that the card is invalid
            //else {return "Card brand not identified";}

            //to comply with the requirements of the exercise, will assume the card is invalid when we can't identify a brand
            else
            {
                return "INVALID\n";
            }

    }

    //AMEX\n start with 34 or 37
    //MASTERCARD\n start with 51, 52, 53, 54, or 55
    //VISA\n start with 4
}


//function to get first 2 digits of a long number
int get_1st_2(long x)
{
    long y = x;
    while (y >= 100)
    {
        y = y / 10;
    }

    return (int) y;
}