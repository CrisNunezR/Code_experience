#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);
int value_char(int char_dec); //we'll use this function to get the value of a char (regardless of upper or lower case)

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int value = 0;//initialises the cumulative value of the word

    //checks each char in the string
    int i = 0;
    while (word[i] != 0)
    {
        value = value + value_char((int) word[i]);
        i++;
    }

    return value;
}

int value_char(int char_dec)
{
    //checks for non-letter values
    if (char_dec < 65 || char_dec > 122)
    {
        return 0;
    }
    //Upper case, return position of array POINTS correspondent to the dec ASCII value - 65
    // dec ASCII of A = 65
    else if (char_dec >= 65 && char_dec <= 90)
    {
        return POINTS[char_dec - 65];
    }
    //Upper case, return position of array POINTS correspondent to the dec ASCII value - 97
    // dec ASCII of A = 97
    else if (char_dec >= 97 && char_dec <= 122)
    {
        return POINTS[char_dec - 97];
    }
    else
    {
        return 0;
    }

}