#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    //JPGs 1st 3 bytes are always the follwing
    //0xff 0xd8 0xff
    //also, the 4th byte always has the form: 0xe?, where ? = 0,1,2,3,4,...,a,b,c,d,e,f,
    //hence, the 1st 4 bits of the 4th byte are always 0xe = 14 = 1110 = 2^3 + 2^2 + 2^1

    //also, cameras tend to store pics one after the other on memory, so the 'start' of a jpg file
    //would define the 'end' of the previous file

    //digital cameras tend to 'initialise' cards with a FAT system with a 'block-size' of 512 bytes
    //this means that these cameras only write on memory in blocks of 512 bytes

    //First we'll validate we got 2 arguments (program + file name)
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //then, we'll define a 8bit = 1byte type in order to read the info in byte-sizes
    //typedef uint8_t BYTE;
    int files_count = 0;    //keeps track of the number of jpegs found
    char file_name[8];      //stores the faile name, accounting for the NUL=/0 char at the end
    bool output_file_open = false;    //we'll use this bool variable to define whether a jpeg was found

    //once validated we got the proper prompt, we open the file
    FILE *input = fopen(argv[1], "r");
    if (input != NULL)
    {
        //setting up variables to use
        unsigned char buffer[512]; //512 byte block to read the file

        //define and open 1st jpeg output file
        sprintf(file_name, "00%i.jpg", files_count);
        printf("%s\n", file_name);

        FILE *output = fopen(file_name, "w");
        if (output == NULL)
        {
            fclose(output);
            printf("Could not write output file %s.\n", file_name);
            return 1;
        }


        while (fread(buffer, sizeof(buffer), 1, input) > 0) //keep reading while we can get 512byte chunks
        {
            //check if JPEG signature is found
            //note: for the last byte we can also use (buffer[3] & 0xf0 which makes the last hex 0 => 0x?0)
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] >= 0xe0 && buffer[3] <= 0xef)
            {

                //jpeg found. Check if the output file's open (which means we've been writing a previous jpeg)
                if (output_file_open == false)
                {
                    //if output bool == false, this is the 1st jpeg
                    //we need to start writing on the output file
                    output_file_open = true;
                    fwrite(buffer, sizeof(buffer), 1, output);
                }

                //if output_file_open == true, we've found the next jpeg
                //we need to close the file, open a new one and start recording data
                else
                {
                    fclose(output);
                    files_count++; //increase the jpeg found counter

                    //define the new output file name
                    if (files_count < 10)
                    {
                        sprintf(file_name, "00%i.jpg", files_count);
                        printf("%s\n", file_name);
                    }
                    else
                    {
                        sprintf(file_name, "0%i.jpg", files_count);
                        printf("%s\n", file_name);
                    }

                    //open new file and start writing on it
                    output = fopen(file_name, "w");
                    if (output != NULL)
                    {
                        // Write block to outfile
                        fwrite(buffer, sizeof(buffer), 1, output);
                    }
                    else //there was a problem writting the output file
                    {
                        fclose(output);
                        printf("Could not write output file %s.\n", file_name);
                        return 1;
                    }
                }
            }

            else if(output_file_open == true)
            {
                //if the block is not a new jpeg and we have an open output file
                //we need to consider the next block as part of the current jpeg and write it
                fwrite(buffer, sizeof(buffer), 1, output);
            }

        }
        fclose(input); //we finished the while loop (and thus the input file) so we need to close it

        //we need to close the last jpeg file and turn the bool to false (for consistency)
        if(output_file_open == true)
        {
            fclose(output);
            output_file_open = false;
        }

    }
    else
    {
        printf("Could not open file.\n");
        return 1;
    }
}