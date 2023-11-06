// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 46;

// Hash table (initially with N = 26 buckets)
node *table[N];

//variable to keep track of the number of words loaded onto the hash-table
int loaded_words = 0;


//******************************************************************************************************

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    //1st: calculate hash_value for the word
    int hash_value;
    hash_value = hash(word);

    //2nd: look at words in hash_table for that hash value
    //to do this, we define a cursor variable that helps us go through the linked list at corresponding the hash_value
    node *cursor;
    cursor = table[hash_value];

    //then we define a while loop that we'll exit when the "next" element is NULL
    char* word_in_dic;
    bool exit = false;
    while (exit == false)
    {
        word_in_dic = cursor->word;
        if (strcasecmp(word_in_dic, word) == 0)
        {
            return true;
        }
        else
        {
            if (cursor->next != NULL)
            {
                cursor = cursor->next;
            }
            else
            {
                exit = true;
                return false;
            }

        }
    }

    return false;
}

//******************************************************************************************************

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    //return toupper(word[0]) - 'A';

    //1st we'll create a simple function that returns the sum of the ascii values
    int ret_value = 0;
    int m = strlen(word);
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        ret_value = ret_value + tolower(word[i]);
    }

    //we use N-1. Initially defined as N-1=25 buckets for the hash-table
    if (ret_value > 0)
    {
        return ret_value%(N - 1);
    }
    else
    {
        printf("Hash function error\n");
        return 1;
    }
}


//******************************************************************************************************

//Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //create variable to store hash values
    int hash_value;

    //open selected dictionary file with words on it
    //printf("%s\n", dictionary);
    FILE *dic_file = fopen(dictionary, "r");
    if (dic_file == NULL)
    {
        printf("Error opening dictionary file %s!\n", dictionary);
        return false;
    }

    //define variable to store each word read from the dictionary
    char word[45+1];

    //read words from dictionary file until End Of File (EOF) is reached
    while (fscanf(dic_file, "%s", word) != EOF)
    {

        //allocate memory space (and store memory location) on new_node to contain new word
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Not enough memory to allocate new word.\n");
            return false;
        }

        //copy word onto new node at the hash-table and define NULL as the next-word value (by default)
        strcpy(new_node->word, word);
        new_node->next = NULL;

        //now we insert the new word (new_node) into the hash table at a location defined by the hash_value

        //step 1: identify hash_value for the new word
        hash_value = hash(new_node->word);

        //step 2: identify whether there are previous words for that hash_value
        if (table[hash_value] == NULL)
        {
            //no previous words for the hash_value in the hash_table
            //step 3: add new word by assigning the addres of new_node to the hash-table at the hash-value
            table[hash_value] = new_node;

            //increase number of loaded words
            loaded_words++;
        }
        else
        {
            //there are some previous elements for the hash_value => insert this new node
            //step 3: assign address on hash-value (previous header) to the "next" element of new_node
            //thus concatenating the already existing linked list to the new_node as the new header
            new_node->next = table[hash_value];

            //step 4: assign address for new_node to the address on hash-value (thus redefinig the header)
            table[hash_value] = new_node;

            //increase number of loaded words
            loaded_words++;
        }
    }

    //load function worked fine
    return true;
}

//******************************************************************************************************

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return loaded_words;
}

//******************************************************************************************************

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *cursor;
    node *tmp;

    //iterate thourgh the table freeing up memory
    for (int i = 0; i < N - 1; i++)
    {
        if (table[i] != NULL)
        {
            cursor = table[i];
            while (cursor->next != NULL)
            {
                tmp = cursor;
                free(tmp);
                cursor = cursor->next;
            }
            free(cursor);
            return true;
        }
    }
    return false;
}
