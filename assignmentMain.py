import assignment


def main():
    word = input("Give a word: ")
    assignment.firstFive(word)
    assignment.lastFive(word)
    assignment.middleFour(word)
    assignment.everyOther(word)
    assignment.backwards(word)


main()