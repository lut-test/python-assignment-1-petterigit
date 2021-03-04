# With the given word, fill in the functions below!
# Modify the variables i&n accordingly to fit the descriptions of the print


def firstFive(word):
    # Hint - This line needs to be i = 5
    i = 5
    print("The first five letters of your word are: " + word[:i])


def lastFive(word):
    # For this one, you are going to need to keep the len(word)
    i = len(word) - 5
    print("The five last letters are: " + word[i:])


def middleFour(word):
    i = 1
    n = 5
    print("Letters 2, 3, 4, and 5 are: " + word[i:n])


def everyOther(word):
    i = 1
    n = 2

    print(
        "Every other letter of the word, starting from the second letter are: "
        + word[i::n]
    )


def backwards(word):
    i = -1
    print("Your word written backwards is: " + word[::i])
