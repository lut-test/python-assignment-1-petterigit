# With the given word, fill in the functions below!
# Modify the variables i&n accordingly to fit the descriptions of the print


def firstFive(word):
    # Hint - This line needs to be i = 5
    i = 5
    return word[:i]


def lastFive(word):
    # For this one, you are going to need to keep the len(word)
    i = len(word) - 5
    return word[i:]


def middleFour(word):
    i = 1
    n = 4
    return word[i:n]


def everyOther(word):
    i = 1
    n = 2

    return word[i::n]


def backwards(word):
    i = -1
    return word[::i]
