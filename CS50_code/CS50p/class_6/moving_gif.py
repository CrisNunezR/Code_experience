"""
This code shows the way to use the PIL library to handle image files

In this case, images[].save is used to 'concatenate' another gif file
(image[1] which is the 2nd argument in the argv (argv[2])
with a delay of duration = 200 ms and an infinite loop (loop=0)

notice that sys.argv[1:] is excluding the name of the code file (moving_gif.py) from the
gif sequence... this also allows the use of many gifs to concatenate as long as their
name is included in the prompt

Execution:
    $ python moving_gif.py costume1.gif costume2.gif

"""

import sys
from PIL import Image

def main():

    images = []

    if len(sys.argv) < 2:
        print("Usage: python moving_gif.py [gif_name_1] [gif_name_2]")
        sys.exit()

    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)

    images[0].save(
        "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
    )

if __name__ == "__main__":
    main()
