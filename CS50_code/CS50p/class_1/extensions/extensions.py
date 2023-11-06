"""
    In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip
"""

def find_extension(str_: str) -> str:
    return str_.find(".", len(str_) - 5)


def main():
    file_name = input("File name: ").replace(" ", "")

    extloc_ = find_extension(file_name)

    if extloc_ == -1:
        print("application/octet-stream")
        return 0
    else:
        ext_ = file_name[extloc_:].lower()

    match ext_:
        case ".gif":
            print("image/gif")
        case ".jpg":
            print("image/jpeg")
        case ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".gif":
            print("image/gif")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")



main()
