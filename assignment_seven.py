# Last Edited: November 12, 2021
# Halley Deme
# This program encodes or decodes text given by the user using the rotation cipher.


def encode(phrase,shift):
    alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    new_phrase=""
    for letter in phrase:
        value = alpha.index(letter)
        value += shift
        new_letter = alpha[value]
        new_phrase += new_letter
    return new_phrase

def decode(phrase,shift):




def main():
    k = input("Please enter a word or phrase you would like to have encoded or decoded")


if __name__ == '__main__':
    main()