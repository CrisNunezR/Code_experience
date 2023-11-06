# TODO

from cs50 import get_string


def main():

    text = get_string('please enter your text: ')

    # letter (L): any lowercase character from a to z or any uppercase character from A to Z
    # word: sequence of characters separated by spaces
    # sentrence (S): any occurrence of a period, exclamation point, or question mark

    L = 0
    S = 0
    W = 0

    for i in (text + " "):
        if i in ['!', '.', '?']:
            S += 1

        if i == " ":
            W += 1

        if i not in [" ", '!', '.', '?', ';', ',', "'"]:
            L += 1

    #print('words: ', W, 'letters: ', L, 'sentences: ', S)


    L = L / W * 100
    S = S / W * 100

    readability = 0.0588 * L - 0.296 * S - 15.8
    #L= avg number of letters in 100 words
    #S= avg number of sentences per 100 words

    if readability < 1:
        print("Before Grade 1")
    elif readability > 16:
        print("Grade 16+")
    else:
        print("Grade ", round(readability))


main()