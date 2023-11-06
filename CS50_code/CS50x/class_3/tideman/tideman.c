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
bool checks_cycle(int loser, int winner, int count); //checks whether a cycle is created

int main(int argc, string argv[])
{
    // Check for invalid usage (if no candidate name is given, prompt error message)
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

    pair_count = 0; //initialises pair_count (value that stores the number of possible pairs)
    int voter_count = get_int("Number of voters: ");

    // Query for votes (for each voter i)
    for (int i = 0; i < voter_count; i++)
    {
        //ranks[i] is voter's ith preference
        //notice that ranks retains the values from the last voter which might allow for errors
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Voter %i, Rank %i: ", i + 1, j + 1);

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

// Update ranks given a new vote
//validates whether the vote was cast for a valid candidate and updates the rank[] array
bool vote(int rank, string name, int ranks[])
{
    // TODO - validate the vote corresponds to a candidate and return false if not
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcasecmp(name, candidates[i]) == 0)
        {
            //registers the vote on array ranks[n° candidates], note that we must do it here since the vote function identifies the location of the candidate/vote cast
            //if vote is valid, register rank 'j' for candidate 'name' on ranks[n], notice that rank[] stores the index of the candidate in candadidates[], not the name
            //rank = j (number of preference in ranks[] array) and i is position of the candidate in the candidates[] array
            ranks[rank] = i;
            return true;
        }
    }
    printf("Candidate name not registered\n");
    return false;
}

// Updates global preferences given every new voter's ranks
void record_preferences(int ranks_[candidate_count])
{
    // TODO -- update the preferences[i][j] array that defines the # of ppl that prefers candidate "i" over candidate "j"
    //remember that ranks stores the number of the candidate for each preference
    // this means that ranks[0] stores the code/number for the most preferred candidate for each voter
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count ; j++)
        {
            preferences[ranks_[i]][ranks_[j]] = preferences[ranks_[i]][ranks_[j]] + 1;
        }
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
                for (int k = 0; k < pair_count; k++)
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
                    //remember that pair_count was initialised to zero before
                    pair_count++;
                    pairs[pair_count-1].winner = i;
                    pairs[pair_count-1].loser = j;
                }
            }
        }
    }

    return;
}

//Sort pairs in decreasing order by strength of victory
//note: we will use a bubble sort type algorithm
void sort_pairs(void)
{
    //a bool variable will be used to check whether a swap took place
    //if it did, we'll recursively call the function again
    bool swapped = false;

    // if there's only one pair, no need to sort
    if (pair_count > 1)
    {
        for (int i = 0; i < pair_count; i++)
        {
            if (preferences[pairs[i].winner][pairs[i].loser] < preferences[pairs[i+1].winner][pairs[i+1].loser])
            {
                int dummy_winner = pairs[i].winner;
                int dummy_loser = pairs[i].loser;

                //swapping values according to strength of victory recorded in preferences array
                pairs[i].winner = pairs[i+1].winner;
                pairs[i].loser = pairs[i+1].loser;

                pairs[i+1].winner = dummy_winner;
                pairs[i+1].loser = dummy_loser;

                swapped = true;
            }
        }
    }

    //recursive call
    if (swapped == true)
    {
        sort_pairs();
    }

    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO: evaluate all pairs and define which ones to lock using the pairs ordered according to victory strength
    for (int i = 0; i < pair_count; i++)
    {
        //add to graph (locked pairs) if no cycle is created
        if (checks_cycle(pairs[i].loser, pairs[i].winner, pair_count) == false)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}

//this function will check whether we can find the winner of the pair we are checking
//as the loser for another pair
bool checks_cycle(int loser, int winner, int count)
{
    for (int i = 0; i < count; i++)
    {
        if (locked[pairs[i].winner][pairs[i].loser] == true) //we only check previously locked pairs
        {
            if (pairs[i].winner == loser) //the loser of the pair we are assessing is the winner of a previously locker pair
            {
                //is the loser of that previously locked pair the winner of the current pair (thus creating a cycle)?
                if (pairs[i].loser == winner)
                {
                    return true; //if yes, we have a cycle
                }
                //if no, we recursivelly call the function to check the rest of the pairs
                //we replace the loser of the first pair with the loser of the current pair
                //we retain the winner of the initial pair we are checking since this is the cycle we are avaluating
                else
                {
                    //notice that is not enough to just call the function recursively, we need to return 'true' in order to "pass it along"
                    if (checks_cycle(pairs[i].loser, winner, pair_count) == true)
                    {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

// Print the winner of the election
void print_winner(void)
{
    //Key concept: the winner is the candidate without any locked pairs in which it is a loser
    bool losers_[candidate_count];

    //sets all candidates to  'not_losers'
    for (int i = 0; i < candidate_count; i++)
    {
        losers_[i] = false;
    }

    //looks at the loser for each locked pair and defines them as losers
    for (int i = 0; i < pair_count; i++)
    {
        if (locked[pairs[i].winner][pairs[i].loser] == true)
        {
            losers_[pairs[i].loser] = true;
        }
    }

    //looks at the candidate array for non-losers and prints out the first
    for (int i = 0; i < candidate_count; i++)
    {
        if (losers_[i] == false)
        {
            printf("%s\n", candidates[i]);
            return;
        }
    }
    return;
}