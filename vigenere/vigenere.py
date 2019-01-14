import cs50
import sys
import itertools


def main():

    if len(sys.argv) != 2:
        print("Usage: vigenere.py key")
        sys.exit(1)
    if not str.isalpha(sys.argv[1]):
        print("Key must be alphabetical")
        sys.exit(1)

    key = sys.argv[1]
    keyLen = len(sys.argv[1])

    plainText = cs50.get_string("plaintext: ")
    print("ciphertext: ", end="")

    # itertools.cycle cylces over the length of key, allowing us to return to the first char in key
    # zip is a way to iterate over two lists in parallel
    # c = characters in plaintext, k = chars in key
    for c, k in zip(plainText, itertools.cycle(key)):
        k = k.upper()
        # ord() converts characters to ASCII values
        k = ord(k)
        k -= 65

        if c.isupper():
            c = ord(c)
            c -= 65
            c = ((c + k) % 26)
            c += 65
            # chr() converts ASCII values to chars
            print(chr(c), end="")
        elif c.islower():
            c = ord(c)
            c -= 97
            c = ((c + k) % 26)
            c += 97
            print(chr(c), end="")
        elif not c.isalpha():
            print(c, end="")

    print()


if __name__ == "__main__":
    main()
