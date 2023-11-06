"""
In a file called shirt.py, implement a program
that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background)
on the input after resizing and cropping the input to be the same size, saving
the result as its output.

Open the input with Image.open, per
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit, per
pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
using default values for method, bleed, and centering, overlay the shirt
with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
and save the result with Image.save, per
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way,
like these demos, so that, when they’re resized and cropped, the shirt appears
to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over
to VS Code’s file explorer, into the same folder as shirt.py. No need to submit any
photos with your code. But, if you would like, you’re welcome (but not expected) to
share a photo of yourself wearing your virtual shirt in any of CS50’s communities!

"""

import sys
from PIL import Image, ImageOps

def main():

    #checks number of arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    #checks the extension of the files are valid
    if not correct_ext(sys.argv[1]):
        sys.exit("Invalid input")
    if not correct_ext(sys.argv[2]):
        sys.exit("Invalid input")

    #checks equal file extensions
    if not equal_ext(sys.argv[1], sys.argv[2]):
        sys.exit("Input and output have different extensions")

    #checks if file exists
    try:
        _ = open(sys.argv[1], 'r')
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

    origin_file = sys.argv[1]
    output_file = sys.argv[2]
    shirt_file = "shirt.png"

    # Open the original image
    original_image = Image.open(origin_file)

    # Open the shirt image and get its size
    overlay_image = Image.open(shirt_file)
    desired_size = overlay_image.size

    # Resize and crop the image using ImageOps.fit. I'm using the size of the shirt.png image and default settings
    resized_image = ImageOps.fit(original_image, desired_size)

    #I initially used this code but the check50 function returned an "Image does not match" error
    #resized_image = ImageOps.fit(original_image, desired_size, method=0, bleed=0.0, centering=(0.5, 0.5))

    """
    Overlay the shirt image on the resized and cropped image to blend the images
    notice that we can also define the overlay position with this alternative:

    overlay_position = (0, 0)
    resized_image.paste(overlay_image, overlay_position, overlay_image)
    """

    resized_image.paste(overlay_image, overlay_image)
    #  the first shirt represents the image to overlay and the second shirt
    #  represents a “mask” indicating which pixels in photo to update.

    # Save the final output image
    resized_image.save(output_file)

    # Close the images
    original_image.close()
    overlay_image.close()

    return 0

#checks correct file extension
def correct_ext(file: str) -> bool:
    ext_idx = len(file) - file.index('.')
    ext = file[-ext_idx:]
    return ext.lower() in ['.jpg', '.jpeg', '.png']

#checks equal file extensions
def equal_ext(file1: str, file2: str) -> bool:
    ext_idx_1 = len(file1) - file1.index('.')
    ext_idx_2 = len(file2) - file2.index('.')

    ext1 = file1[-ext_idx_1:]
    ext2 = file2[-ext_idx_2:]

    return  ext1 == ext2





if __name__ == "__main__":
    main()