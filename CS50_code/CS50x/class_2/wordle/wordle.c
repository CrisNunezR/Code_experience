#include <cs50.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

// each of our text files contains 1000 words
#define LISTSIZE 1000

// values for colors and score (EXACT == right letter, right place; CLOSE == right letter, wrong place; WRONG == wrong letter)
#define EXACT 2
#define CLOSE 1
#define WRONG 0

// ANSI color codes for boxed in letters
#define GREEN   "\e[38;2;255;255;255;1m\e[48;2;106;170;100;1m"
#define YELLOW  "\e[38;2;255;255;255;1m\e[48;2;201;180;88;1m"
#define RED     "\e[38;2;255;255;255;1m\e[48;2;220;20;60;1m"
#define RESET   "\e[0;39m"

// user-defined function prototypes
string get_guess(int wordsize);
int check_word(string guess, int wordsize, int status[], string choice);
void print_word(string guess, int wordsize, int status[]);
int word_size(string str_guess);
bool letter_in_string(char chr, string word);

int main(int argc, string argv[])
{
    // ensure proper usage
    // TODO #1
    if (argc != 2)
    {
        printf("Usage: ./wordle wordsize\n");
        return 1;
    }

    int wordsize = 0;

    // ensure argv[1] is either 5, 6, 7, or 8 and store that value in wordsize instead
    // TODO #2
    //usage of strtol converter from char to int: long int strtol([string], reference to type of char, [int base from 2 to 36])
    char *p;
    wordsize = strtol(argv[1], &p, 10);

    if (wordsize < 5 || wordsize > 8)
    {
        printf("Error: wordsize must be either 5, 6, 7, or 8\n");
        return 1;
    }

    // open correct file, each file has exactly LISTSIZE words
    char wl_filename[6];
    sprintf(wl_filename, "%i.txt", wordsize);
    FILE *wordlist = fopen(wl_filename, "r");
    if (wordlist == NULL)
    {
        printf("Error opening file %s.\n", wl_filename);
        return 1;
    }

    // load word file into an array of size LISTSIZE (notice that LISTSIZE has been redefined as 1000)
    char options[LISTSIZE][wordsize + 1];

    for (int i = 0; i < LISTSIZE; i++)
    {
        fscanf(wordlist, "%s", options[i]);
    }

    // pseudorandomly select a word for this game
    srand(time(NULL));
    string choice = options[rand() % LISTSIZE];

    // allow one more guess than the length of the word
    int guesses = wordsize + 1;
    bool won = false;

    // print greeting, using ANSI color codes to demonstrate
    printf(GREEN"This is WORDLE50"RESET"\n");
    printf("You have %i tries to guess the %i-letter word I'm thinking of\n", guesses, wordsize);

    // main game loop, one iteration for each guess
    for (int i = 0; i < guesses; i++)
    {
        // obtain user's guess
        string guess = get_guess(wordsize);

        // array to hold guess status, initially set to zero
        int status[wordsize];

        // set all elements of status array initially to 0, aka WRONG
        // TODO #4
        for (int j = 0; j < wordsize; j++)
        {
            status[j] = 0;
        }

        // Calculate score for the guess
        int score = check_word(guess, wordsize, status, choice);

        printf("Guess %i: ", i + 1);

        // Print the guess with coloured status for each letter
        print_word(guess, wordsize, status);

        // if they guessed it exactly right, set terminate loop
        if (score == EXACT * wordsize)
        {
            won = true;
            break;
        }
    }

    // Print the game's result
    // TODO #7
    if (won)
    {
        printf("You won!\n");
    }
    else
    {
        printf("The word to guess was: %s\n", choice);
    }

    // that's all folks!
    return 0;
}

//function to get the word guessed by the user, validating its size before returning it
string get_guess(int wordsize)
{
    string guess = "";

    // ensure users actually provide a guess that is the correct length
    // TODO #3
    do
    {
        guess = get_string("Input a %i-letter word: ", wordsize);
    }
    while (word_size(guess) != wordsize);

    return guess;
}

int check_word(string guess, int wordsize, int status[], string choice)
{
    int score = 0;

    // compare guess to choice and score points as appropriate, storing points in status
    // TODO #5
    // Status values for each letter: EXACT 2 | CLOSE 1 | WRONG 0
    int i;

    for (i = 0; i < wordsize; i++)
    {
        if (guess[i] == choice[i])
        {
            status[i] = 2;  //status EXACT
            score = score + 2;
        }
        else if (letter_in_string(guess[i], choice))
        {
            status[i] = 1; //status CLOSE
            score = score + 1;
        }
        else
        {
            status[i] = 0; //status WRONG
        }
    }
    // HINTS
    // iterate over each letter of the guess
    // iterate over each letter of the choice
    // compare the current guess letter to the current choice letter
    // if they're the same position in the word, score EXACT points (green) and break so you don't compare that letter further
    // if it's in the word, but not the right spot, score CLOSE point (yellow)
    // keep track of the total score by adding each individual letter's score from above

    return score;
}

void print_word(string guess, int wordsize, int status[])
{
    // print word character-for-character with correct color coding, then reset terminal font to normal
    // TODO #6
    for (int k = 0; k < wordsize; k++)
    {
        switch (status[k])
        {
            case 0:
                printf(RED"%c"RESET, guess[k]);
                break;
            case 1:
                printf(YELLOW"%c"RESET, guess[k]);
                break;
            case 2:
                printf(GREEN"%c"RESET, guess[k]);
        }
    }


    printf("\n");
    return;
}

//fuction that returns the leght of a string
int word_size(string str_guess)
{
    int i = 0;
    while (str_guess[i] != 0)
    {
        i++;
    }
    return i;
}

//function that returns True if a character exists within a word and false if it doesn't
bool letter_in_string(char chr, string word)
{
    int i = 0;
    do
    {
        if ((int) word[i] == (int) chr)
        {
            return true;
            //break;
        }
        i++;
    }
    while (word[i] != 0);

    return false;
}