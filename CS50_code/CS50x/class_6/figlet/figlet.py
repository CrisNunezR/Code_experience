#include figlet
#pip install pyfiglet
import sys

from pyfiglet import Figlet
#f=Figlet(font='slant')
#print(f.renderText('text'))

figlet = Figlet()
#figlet.getFonts()

#to define optional arguments, we just assign a value to the variable
def main(cmd_ = '-f', font_ = 'slant'):

    #print("after calling function:", sys.argv[1:])
    #define a list of available fonts
    list_fonts = figlet.getFonts()

    #print font
    #print(font_)
    #print(cmd_)

    #if paramenters entered are wrong, exit
    if (cmd_ != '-f' and cmd_ != '--font'):
        sys.exit('Invalid usage')
    elif (font_ not in list_fonts):
        sys.exit('Invalid usage')

    #if no problem encountered, continue printing

    #ask for text to print out
    text = input("Please, enter text to print out: ")

    #print(list_fonts)

    #print out according to given font
    figlet.setFont(font = font_)
    print(figlet.renderText(text))

#execute main()
if __name__ == "__main__":
    #print("before calling function:" , sys.argv[1:])
    main(sys.argv[1], sys.argv[2]) #notice that we call the main with arguments excluding self = arg[0]
