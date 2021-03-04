# With the given word, fill in the functions below!
# Modify the variables i&n accordingly to fit the descriptions of the print


def firstFive(word):
    # Hint - This line needs to be i = 5
    i = len(word)
    print("The first five letters of your word are: " + word[:i])


def lastFive(word):
    # For this one, you are going to need to keep the len(word)
    i = len(word) - 0
    print("The five last letters are: " + word[i:])


def middleFour(word):
    i = 0
    n = len(word)
    print("Letters 2, 3, 4, and 5 are: " + word[i:n])


def everyOther(word):
    i = 0
    n = 1

    print(
        "Every other letter of the word, starting from the second letter are: "
        + word[i::n]
    )


def backwards(word):
    i = 1
    print("Your word written backwards is: " + word[::i])


def main():
    word = input("Give a word: ")
    firstFive(word)
    lastFive(word)
    middleFour(word)
    everyOther(word)
    backwards(word)


main()