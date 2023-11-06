#include <cs50.h>
#include <stdio.h>


int count_letters(string text);
int count_sentences(string text);
int count_words(string text);

int main(void)
{
    string text = get_string("Please enter text: ");

    //printf("Letters: %i\nSentences: %i\nWords: %i\n", count_letters(text), count_sentences(text), count_words(text));

    double L = 100 * (count_letters(text) / (double) count_words(text));
    double S = 100 * (count_sentences(text) / (double) count_words(text));

    //printf("Grade: %f\nL: %f\nS:%f\n", 0.0588 * L - 0.296 * S - 15.8, L, S);

    double readability =  0.0588 * L - 0.296 * S - 15.8;

    //readability 16 or higher => return "Grade 16+"
    //redeability < 1 => return "Before Grade 1"
    if (readability < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (readability >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", readability);
    }

    //printf("Grade: %.0f\n", 0.0588 * L - 0.296 * S - 15.8);

}

//this function returns the number of letters within a text
//letter is any lowercase character from a to z or any uppercase character from A to Z
int count_letters(string text)
{
    int count_letters = 0;

    int i = 0;
    while (text[i] != 0)
    {
        //if character is an upper or lower letter, increment the counter
        if (((int) text[i] >= 65 && (int) text[i] <= 90) || ((int) text[i] >= 97 && (int) text[i] <= 122))
        {
            count_letters++;
        }
        i++;
    }

    return count_letters;
}
//function counts sentences
//any occurrence of a period, exclamation point, or question mark indicates the end of a sentence
int count_sentences(string text)
{
    //ASCII dec values
    // .: 46
    // !: 33
    // ?: 63
    int counter = 0; // we assume we need to end with a period

    int i = 0;
    while (text[i] != 0)
    {
        if ((int) text[i] == 46 || (int) text[i] == 33 || (int) text[i] == 63)
        {
            counter++;
        }

        i++;
    }

    return counter;
}


//function counts words in a text
//any sequence of characters separated by spaces counts as a word
int count_words(string text)
{
    //ASCII dec values
    // ' ': 32
    int counter = 1;

    int i = 1; // we assume we have at least 1 word
    while (text[i] != 0)
    {
        if ((int) text[i] == 32)
        {
            counter++;
        }

        i++;
    }

    return counter;
}