#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtBlue == 00 && image[i][j].rgbtGreen == 00 && image[i][j].rgbtRed == 00)
            {
                //remember that to handle hex we need to "tell" the program the value is hex, this is done using 0x before the value
                image[i][j].rgbtBlue = 0x00;
                image[i][j].rgbtGreen = 0xFF;
                image[i][j].rgbtRed = 0x00;
            }
        }
    }
}
