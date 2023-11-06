#include <stdio.h>
#include <string.h> //library needed to use strcopy
#include <stdlib.h> //library to use malloc and free

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    char *plates[8];

    //open a file to "r" read
    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // Save plate number in array
        //notice that strings store memory location, not values,
        //so plates[] is a pointer that stores memory location of the 1st char in 'buffer' for every iteration
        //plates[idx] = buffer;

        //to correctly copy the strings, we can use another variable "t" to store the location of enough memory
        //remember that malloc returns the address of the 1st byte for the memory block we requested
        char *t = malloc(7);
        if (t == NULL)
        {
            return 1;   //this is a safeguard we must use to avoid continuing when we try to allocate more memory than available
        }
        //then copy the current string we got from the file and store it at that memory location
        strcpy(t, buffer);
        //then finally copy the memory location to the corresponding value of plates[]
        //notice that we must assign only the memory location of t[0] since we are working with strings and
        //we only need the 1st char
        plates[idx] = &t[0];

        idx++;

    }

    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);
    }

    //return 0;
    free(infile);

}
