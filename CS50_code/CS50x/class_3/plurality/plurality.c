#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);
void order(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1]; //notice that argv[0] is the name of the program
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote[%i]: ", i + 1);

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // compare 'name' with the candidates (name values in the struct)
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcasecmp(name, candidates[i].name) == 0)
        {
            //update count
            candidates[i].votes = candidates[i].votes + 1;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
//since we are supposed to return all the winners were there to be a tie
//it is best to order the array and then print out the candidate(s) that achieve the highest number of votes
void print_winner(void)
{
    // TODO
    order();

    //this code is useful if we need to print out just one winner
    //and the struct is not expected to be sorted
    //int max_ = candidates[0].votes;
    //int max_i = 0;
    //for (int i = 0; i < candidate_count; i++)
    //{
    //    if (max_ < candidates[i].votes)
    //    {
    //        max_ = candidates[i].votes;
    //        max_i = i;
    //    }
    //}
    //printf("%s\n", candidates[max_i].name);

    //if the list is sorted, we can assume the 1st name is the winner
    //we just need to identify whether there's more candidates with the same result
    printf("%s\n", candidates[0].name);     //print out the 1st place
    for (int i = 1; i < candidate_count; i++)
    {
        if (candidates[i].votes == candidates[0].votes)
        {
            printf("%s\n", candidates[i].name);
        }
        else
        {
            return;     // if the next candidate does not have equal votes, no need to keep searching
        }
    }
    return;
}

//function to order the array
void order(void)
{
    bool ordered = true;   //keeps track of whether the list is ordered
    string dummy_name = "";
    int dummy_votes = 0;

    //bubble ordering
    int i = 0;
    while (i < candidate_count - 1)
    {
        if (candidates[i].votes < candidates[i + 1].votes)
        {
            //swapping values
            dummy_name = candidates[i + 1].name;
            dummy_votes = candidates[i + 1].votes;

            candidates[i + 1].votes = candidates[i].votes;
            candidates[i + 1].name = candidates[i].name;
            candidates[i].votes = dummy_votes;
            candidates[i].name = dummy_name;

            //regirsters that there was a swapp made
            ordered = false;
         }

         //if no swap is made, break the loop, otherwise, run again
        if (!ordered)
        {
            ordered = true;
            i = 0;
        }
        else
        {
            i++;
        }

    }
}