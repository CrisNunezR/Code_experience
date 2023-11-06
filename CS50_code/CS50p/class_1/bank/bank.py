

def main():
    grt = input("Greeting: ").replace(" ", "").lower()

    if grt[:5] == "hello":
        print("$0")
    elif grt[:1] == "h":
        print("$20")
    else:
        print("$100")



main()