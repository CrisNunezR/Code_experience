"""
In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
    Zero if the user would like to output text in a random font.

    Two if the user would like to output text in a specific font,
    in which case the first of the two should be -f or --font, and
    the second of the two should be the name of the font.

    Prompts the user for a str of text.

    Outputs that text in the desired font.

    If the user provides two command-line arguments and the first
    is not -f or --font or the second is not the name of a font,
    the program should exit via sys.exit with an error message.
"""

import random
import sys
from pyfiglet import Figlet

def main():

    #supported fonts acccording to "view-source:http://www.figlet.org/examples.html"
    sup_fonts = [
        '3-d',
        '3x5',
        '5lineoblique',
        'acrobatic',
        'alligator',
        'alligator2',
        'alphabet',
        'avatar',
        'banner',
        'banner3',
        'banner3-D',
        'banner4',
        'barbwire',
        'basic',
        'bell',
        'big',
        'bigchief',
        'binary',
        'block',
        'bubble',
        'bulbhead',
        'calgphy2',
        'caligraphy',
        'catwalk',
        'chunky',
        'coinstak',
        'colossal',
        'computer',
        'contessa',
        'contrast',
        'cosmic',
        'cosmike',
        'cricket',
        'cyberlarge',
        'cybermedium',
        'cybersmall',
        'diamond',
        'digital',
        'doh',
        'doom',
        'dotmatrix',
        'drpepper',
        'eftichess',
        'eftifont',
        'eftipiti',
        'eftirobot',
        'eftitalic',
        'eftiwall',
        'eftiwater',
        'epic',
        'fender',
        'fourtops',
        'fuzzy',
        'goofy',
        'gothic',
        'graffiti',
        'hollywood',
        'invita',
        'isometric1',
        'isometric2',
        'isometric3',
        'isometric4',
        'italic',
        'ivrit',
        'jazmine',
        'jerusalem',
        'katakana',
        'kban',
        'larry3d',
        'lcd',
        'lean',
        'letters',
        'linux',
        'lockergnome',
        'madrid',
        'marquee',
        'maxfour',
        'mike',
        'mini',
        'mirror',
        'mnemonic',
        'morse',
        'moscow',
        'nancyj',
        'nancyj-fancy',
        'nancyj-underlined',
        'nipples',
        'ntgreek',
        'o8',
        'ogre',
        'pawp',
        'peaks',
        'pebbles',
        'pepper',
        'poison',
        'puffy',
        'pyramid',
        'rectangles',
        'relief',
        'relief2',
        'rev',
        'roman',
        'rot13',
        'rounded',
        'rowancap',
        'rozzo',
        'runic',
        'runyc',
        'sblood',
        'script',
        'serifcap',
        'shadow',
        'short',
        'slant',
        'slide',
        'slscript',
        'small',
        'smisome1',
        'smkeyboard',
        'smscript',
        'smshadow',
        'smslant',
        'smtengwar',
        'speed',
        'stampatello',
        'standard',
        'starwars',
        'stellar',
        'stop',
        'straight',
        'tanja',
        'tengwar',
        'term',
        'thick',
        'thin',
        'threepoint',
        'ticks',
        'ticksslant',
        'tinker-toy',
        'tombstone',
        'trek',
        'tsalagi',
        'twopoint',
        'univers',
        'usaflag',
        'weird'
    ]

    #if only name of code given as argument, select a random font
    if len(sys.argv) == 1:
        font_ = random.choice(sup_fonts)
    #if not enough arguments or calling font erroneously, exit
    elif sys.argv[1] not in ["-f", "-font"] or len(sys.argv) != 3:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3:
        font_ = sys.argv[2]

    #validates that font is supported
    try:
        f = Figlet(font = font_) #defines the font
    except:
        sys.exit("Invalid usage")

    str_ =  input("Input: ")

    print("Output:\n", f.renderText(str_))


if __name__ == "__main__":
    main()