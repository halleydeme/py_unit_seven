
def printing(word):
    print(word.upper())
    print(word.lower())
def main():
    name = input("Please enter a word.")
    printing(name)
    printing_letters(name)

def printing_letters(word):
    for letter in word:
        print(letter)



if __name__ == '__main__':
    main()