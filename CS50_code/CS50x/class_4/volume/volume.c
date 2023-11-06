// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

//define 2 data_types for the header and the data
typedef uint8_t BYTE;       //BYTE is defined as a 1-BYTE variable
typedef int16_t BYTE2;      //BYTE2 is defined as a 2-byte variable (16-bits)

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    //we define an array header with 44 bytes as defined by HEADER_SIZE
    BYTE header[HEADER_SIZE];

    // TODO: Copy header from input file to output file
    //now we read the header from the 'input' file and store it on the header array
    fread(header, HEADER_SIZE, 1, input);

    //after this, we write the the array header to the 'output' file
    fwrite(header, HEADER_SIZE, 1, output);

    //now, to handle the info from the wave file, we create a new 2-byte size variable 'sample'
    //to store bytes of info that we will then multipy by the factor and save to the output file
    //remember that the info in the wav file is stored in 2-bytes chuncks
    BYTE2 sample;

    //printf("size of BYTE2: %lu\n", sizeof(BYTE2));

    // TODO: Read samples from input file and write updated data to output file
    while (fread(&sample, sizeof(BYTE2), 1, input))
    {
        sample *= factor; //now we redefine sample as sample * factor. note that we don't need to use malloc here

        fwrite(&sample, sizeof(BYTE2), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
