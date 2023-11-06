#include <cs50.h>
#include <stdio.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        //ranks[i] is voter's ith preference
        //note that this array is defined within the For Loop, meaning that it is not avalilable once a given loop is done with
        int ranks[candidate_count];

        // Query to rank candidate according to ranks 'j'
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Voter %i, Rank %i: ", i + 1, j + 1);

            //updates rank with every new vote
            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        // Updates global preferences given every newly registered voter's ranks
        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

//validates whether the vote was cast for a valid candidate and unpdates the rank[] array
bool vote(int rank, string name, int ranks[])
{
    // TODO - validate the vote corresponds to a candidate and return false if not
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcasecmp(name, candidates[i]) == 0)
        {
            return true;

            //registers the vote on array ranks[n° candidates], note that we must do it here since the vote function identifies the location of the candidate/vote cast
            //if vote is valid, register rank 'j' for candidate 'name' on ranks[n], notice that rank[] stores the index of the candidate in candadidates[], not the name
            //rank = j (number of preference in ranks[] array) and i is position of the candidate in the candidates[] array
            ranks[rank] = i;
        }
    }
    return false;
}

// Updates global preferences given every new voter's ranks
void record_preferences(int ranks[])
{
    // TODO -- update the preferences[i][j] array that defines the # of ppl that prefers candidate "i" over candidate "j"
    //remember that ranks stores the number of the candidate for each preference
    // this means that ranks[0] stores the code/number for the most preferred candidate for each voter
    for (int i = 0; i < candidate_count - 1; i++)
    {
        preferences[ranks[i]][ranks[i + 1]] = preferences[ranks[i]][ranks[i + 1]] + 1;
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO -- count the number of pairs
    bool not_new_pair = false;
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            // identifies if one pair's preferences is larger that its counterpart (this excludes cases with zero votes as well)
            if (preferences[i][j] > preferences[j][i])
            {
                //check whether the pair is already included
                for (int k = 0; pair_count; k++)
                {
                    //if pair is not new, create a new pair
                    if (pairs[k].winner == i && pairs[k].loser == j)
                    {
                        not_new_pair = true;
                    }
                }

                //if pair is new, increase counter and include in pair array
                if (!not_new_pair)
                {
                    pair_count++;
                    pairs[pair_count-1].winner = i;
                    pairs[pair_count-1].loser = j;
                }

            }
        }
    }

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        printf("preference winner: %i, Loser: %i, total preference: %i\n", pairs[i].winner, pairs[i].loser, preferences[pairs[i].winner][pairs[i].loser]);
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    return;
}