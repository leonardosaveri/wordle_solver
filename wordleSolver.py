from scoringWord import *
from inputTry import *

with open("WordList.txt", "r") as f:
    wordList = [line.rstrip() for line in f]


ans = ["-", "-", "-", "-", "-"]
notIn = []
inside = dict()
c = 1
while c:
    best = get_best(wordList)
    print(f"We suggest trying with: {best}")
    if input("Found the solution? (y/n)\n").lower() == "y":
        break
    ans, notIn, inside = ask_correct(ans, notIn, inside, best)
    wordList = remove_from_letters(wordList, notIn)
    wordList = only_with_green(wordList, ans)
    wordList = only_with_yellow(wordList, inside)
    c += 1
print("Thank for using the program! I solved the wordle in " + str(c) + " try" if c == 1 else
      "Thank for using the program! I solved the wordle in " + str(c) + " tries")
