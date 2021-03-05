import assignment


def main():
    word = input("Give a word: ")
    print("The first five letters of your word are: " + assignment.firstFive(word))
    print("The five last letters are: " + assignment.lastFive(word))
    print("Letters 2, 3, 4, and 5 are: " + assignment.middleFour(word))
    print(
        "Every other letter of the word, starting from the second letter are: "
        + assignment.everyOther(word)
    )
    print("Your word written backwards is: " + assignment.backwards(word))


main()