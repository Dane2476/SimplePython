from cs50 import get_int


def main():

    while True:
        height = get_int("Height: ")
        if height >= 0 and height <= 23:
            break

    spaces = height - 1
    hashes = 2

    for i in range(height):
        print(" " * spaces, end="")
        print("#" * hashes, end="")
        print("")
        spaces -= 1
        hashes += 1


if __name__ == "__main__":
    main()