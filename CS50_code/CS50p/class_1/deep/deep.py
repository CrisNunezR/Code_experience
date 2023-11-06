#conditionals training code

def main():
    _ = input("What's the Answer to the Great Question of Life, the Universe, and Everything? ").lower().replace(" ", "")

    if _ == "42" or _ == "forty-two" or _ == "forty two":
        print('Yes')
    else:
        print("No")

main()