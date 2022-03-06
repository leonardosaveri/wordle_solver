from scoringWord import *
from inputTry import *

with open("WordList.txt", "r") as f:
    wordList = [line.rstrip() for line in f]


ans = ["-", "-", "-", "-", "-"]
notIn = []
inside = dict()
c = 1
while c:
    print(f"We suggest trying with: {get_best(wordList)}")
    choice = input("What word do you choose:\n")
    best = choice if choice in wordList else get_best(wordList)
    guess = input("Input the solution, "
                  "use uppercase for letters in position, "
                  "lowercase for letters included but not in place "
                  "and \'-\' for empty (Example: L-a-i)\n")
    if guess.lower() == best.lower():
        break
    ans, notIn, inside = ask_correct(guess, ans, notIn, inside, best)
    wordList = remove_from_letters(wordList, notIn)
    wordList = only_with_green(wordList, ans)
    wordList = only_with_yellow(wordList, inside)
    c += 1
print("Thank for using the program! I solved the wordle in " + str(c) + " try" if c == 1 else
      "Thank for using the program! I solved the wordle in " + str(c) + " tries")
