#include "helpers.h"
#include <stdlib.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //create a temp variable to store the newly calculated value of the gray pixel
    float temp;

    //go through all the 'pixels' from top to bottom and left to right
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp = image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed;
            temp = temp / 3;
            temp = round(temp);
            image[i][j].rgbtBlue = temp;
            image[i][j].rgbtGreen = temp;
            image[i][j].rgbtRed = temp;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //create a temp variables for each sepia altered colour
    float sepiaRed;
    float sepiaGreen;
    float sepiaBlue;

    //go through the image pixel by pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //assigning sepia values
            sepiaRed = (0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            sepiaGreen = (0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            sepiaBlue = (0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);

            //controlling boudaries for resulted calculation
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            //updating values to sepia
            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtBlue = round(sepiaBlue);
            image[i][j].rgbtGreen = round(sepiaGreen);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //create temp variables to pass values between sides of the image
    //notice that we don't need float variables here since we are not calculating values
    //but just passing them to other location
    BYTE temp_B;
    BYTE temp_G;
    BYTE temp_R;

    //go through all the 'pixels' from top to bottom and left to right
    for (int i = 0; i < height; i++)
    {
        int width_ = (int)floor(width/2); //notice that we only need to go through the image up to its half point horizontaly
        for (int j = 0; j < width_; j++)
        {
            //take pixel and swap it for the one on the right side
            temp_G = image[i][j].rgbtGreen;
            temp_B = image[i][j].rgbtBlue;
            temp_R = image[i][j].rgbtRed;

            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;

            image[i][width - j - 1].rgbtRed = temp_R;
            image[i][width - j - 1].rgbtBlue = temp_B;
            image[i][width - j - 1].rgbtGreen = temp_G;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //create temp values for each colour
    float temp_B;
    float temp_G;
    float temp_R;

    //we need to create an array to store the calculated values in order to avoid affecting
    //the new value of each pixel by using the newly calculated pixels
    RGBTRIPLE(*image_)[width] = calloc(height, width * sizeof(RGBTRIPLE));

    //the 'problem' with the blur algorithm lies on the border of the image
    //to simplify, first let's take all pixels avoiding the borders
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
           if (i == 0)
           {
                //this section covers cases for the top row
                if (j == 0)
                {
                    //top left corner
                    //sum( [0,1], [0,1])
                    temp_B = image[i][j].rgbtBlue + image[i][j+1].rgbtBlue;
                    temp_B = temp_B + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue;

                    temp_R = image[i][j].rgbtRed + image[i][j+1].rgbtRed;
                    temp_R = temp_R + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed;

                    temp_G = image[i][j].rgbtGreen + image[i][j+1].rgbtGreen;
                    temp_G = temp_G + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen;

                    temp_B = temp_B / 4;
                    temp_G = temp_G / 4;
                    temp_R = temp_R / 4;
                }
                else if(j == width - 1)
                {
                    //top right corner
                    //sum([0,1], [-1,0])
                    temp_B = image[i][j-1].rgbtBlue + image[i][j].rgbtBlue;
                    temp_B = temp_B + image[i+1][j-1].rgbtBlue + image[i+1][j].rgbtBlue;

                    temp_R = image[i][j-1].rgbtRed + image[i][j].rgbtRed;
                    temp_R = temp_R + image[i+1][j-1].rgbtRed + image[i+1][j].rgbtRed;

                    temp_G = image[i][j-1].rgbtGreen + image[i][j].rgbtGreen;
                    temp_G = temp_G + image[i+1][j-1].rgbtGreen + image[i+1][j].rgbtGreen;

                    //calculating average
                    temp_B = temp_B / 4;
                    temp_G = temp_G / 4;
                    temp_R = temp_R / 4;
                }

                else
                {
                    //top border at middle
                    //sum([0,1], [-1,+1])
                    temp_B = image[i][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue;
                    temp_B = temp_B + image[i+1][j-1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue;

                    temp_R = image[i][j-1].rgbtRed + image[i][j].rgbtRed + image[i][j+1].rgbtRed;
                    temp_R = temp_R + image[i+1][j-1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed;

                    temp_G = image[i][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen;
                    temp_G = temp_G + image[i+1][j-1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen;

                    //calculating average
                    temp_B = temp_B / 6;
                    temp_G = temp_G / 6;
                    temp_R = temp_R / 6;
                }
           }

           else if(i == height - 1)
           {
                //this section covers cases at the bottom row
                if(j == 0)
                {
                    //bottom left corner
                    //sum([-1,0], [0,1])
                    temp_B = image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue;
                    temp_B = temp_B + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue;

                    temp_R = image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed;
                    temp_R = temp_R + image[i][j].rgbtRed + image[i][j+1].rgbtRed;

                    temp_G = image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen;
                    temp_G = temp_G + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen;

                    //calculating average
                    temp_B = temp_B / 4;
                    temp_G = temp_G / 4;
                    temp_R = temp_R / 4;
                }

                else if(j == width - 1)
                {
                    //bottom right corner
                    //sum([-1,0], [-1,0])
                    temp_B = image[i-1][j-1].rgbtBlue + image[i-1][j].rgbtBlue;
                    temp_B = temp_B + image[i][j-1].rgbtBlue + image[i][j].rgbtBlue;

                    temp_R = image[i-1][j-1].rgbtRed + image[i-1][j].rgbtRed;
                    temp_R = temp_R + image[i][j-1].rgbtRed + image[i][j].rgbtRed;

                    temp_G = image[i-1][j-1].rgbtGreen + image[i-1][j].rgbtGreen;
                    temp_G = temp_G + image[i][j-1].rgbtGreen + image[i][j].rgbtGreen;

                    //calculating average
                    temp_B = temp_B / 4;
                    temp_G = temp_G / 4;
                    temp_R = temp_R / 4;
                }

                else
                {
                    //bottom row at middle
                    //sum([-1,0],[-1,+1])
                    temp_B = image[i-1][j-1].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue;
                    temp_B = temp_B + image[i][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue;

                    temp_R = image[i-1][j-1].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed;
                    temp_R = temp_R + image[i][j-1].rgbtRed + image[i][j].rgbtRed + image[i][j+1].rgbtRed;

                    temp_G = image[i-1][j-1].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen;
                    temp_G = temp_G + image[i][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen;

                    //calculating average
                    temp_B = temp_B / 6;
                    temp_G = temp_G / 6;
                    temp_R = temp_R / 6;
                }
            }

            else //this section covers cases not on top nor bottom rows
            {
                if(j == 0)
                {
                    //left border at middle
                    //sum([-1,+1],[0,+1])
                    temp_B = image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue;
                    temp_B = temp_B + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue;
                    temp_B = temp_B + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue;

                    temp_R = image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed;
                    temp_R = temp_R + image[i][j].rgbtRed + image[i][j+1].rgbtRed;
                    temp_R = temp_R + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed;

                    temp_G = image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen;
                    temp_G = temp_G + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen;
                    temp_G = temp_G + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen;

                    //calculating average
                    temp_B = temp_B / 6;
                    temp_G = temp_G / 6;
                    temp_R = temp_R / 6;
                }
                else if(j == width - 1)
                {
                    //right border at middle
                    //sum([-1,+1],[-1,0])
                    temp_B = image[i-1][j-1].rgbtBlue + image[i-1][j].rgbtBlue;
                    temp_B = temp_B + image[i][j-1].rgbtBlue + image[i][j].rgbtBlue;
                    temp_B = temp_B + image[i+1][j-1].rgbtBlue + image[i+1][j].rgbtBlue;

                    temp_R = image[i-1][j-1].rgbtRed + image[i-1][j].rgbtRed;
                    temp_R = temp_R + image[i][j-1].rgbtRed + image[i][j].rgbtRed;
                    temp_R = temp_R + image[i+1][j-1].rgbtRed + image[i+1][j].rgbtRed;

                    temp_G = image[i-1][j-1].rgbtGreen + image[i-1][j].rgbtGreen;
                    temp_G = temp_G + image[i][j-1].rgbtGreen + image[i][j].rgbtGreen;
                    temp_G = temp_G + image[i+1][j-1].rgbtGreen + image[i+1][j].rgbtGreen;

                    //calculating average
                    temp_B = temp_B / 6;
                    temp_G = temp_G / 6;
                    temp_R = temp_R / 6;
                }

                else
                {
                    //middle cases, not on any border
                    //sum([-1,+1],[-1,+1])
                    temp_B = image[i-1][j-1].rgbtBlue + image[i-1][j].rgbtBlue + image[i-1][j+1].rgbtBlue;
                    temp_B = temp_B + image[i][j-1].rgbtBlue + image[i][j].rgbtBlue + image[i][j+1].rgbtBlue;
                    temp_B = temp_B + image[i+1][j-1].rgbtBlue + image[i+1][j].rgbtBlue + image[i+1][j+1].rgbtBlue;

                    temp_R = image[i-1][j-1].rgbtRed + image[i-1][j].rgbtRed + image[i-1][j+1].rgbtRed;
                    temp_R = temp_R + image[i][j-1].rgbtRed + image[i][j].rgbtRed + image[i][j+1].rgbtRed;
                    temp_R = temp_R + image[i+1][j-1].rgbtRed + image[i+1][j].rgbtRed + image[i+1][j+1].rgbtRed;

                    temp_G = image[i-1][j-1].rgbtGreen + image[i-1][j].rgbtGreen + image[i-1][j+1].rgbtGreen;
                    temp_G = temp_G + image[i][j-1].rgbtGreen + image[i][j].rgbtGreen + image[i][j+1].rgbtGreen;
                    temp_G = temp_G + image[i+1][j-1].rgbtGreen + image[i+1][j].rgbtGreen + image[i+1][j+1].rgbtGreen;

                    //calculating average
                    temp_B = temp_B / 9;
                    temp_G = temp_G / 9;
                    temp_R = temp_R / 9;
                }
            }

            //redefine pixels with blurred values
            image_[i][j].rgbtBlue = round(temp_B);
            image_[i][j].rgbtRed = round(temp_R);
            image_[i][j].rgbtGreen = round(temp_G);
           }
        }

        //now we update the original image array and then let go the allocated memory on image_
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                image[i][j] = image_[i][j];
            }
        }

        free(image_);

    return;
}
