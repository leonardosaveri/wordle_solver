def ask_correct(ans, notIn, inside, best):
    guess = input("Input the solution, "
                  "use uppercase for letters in position, "
                  "lowercase for letters included but not in place "
                  "and \'-\' for empty (Example: L-a-i)\n")
    for i in range(len(guess)):
        if guess[i] == "-":
            notIn += best[i]
        elif guess[i].isupper():
            if ans[i] == "-":
                ans[i] = guess[i].lower()
        else:
            if i+1 in inside:
                inside[i+1].append(guess[i])
            else:
                inside[i+1] = [guess[i]]
    # this is not definitive, have to find a way to account for double
    for i in notIn:
        if i in ans:
            notIn.remove(i)
    print(f"The letters that are not in are: {notIn}")
    return ans, notIn, inside


# this one works
def remove_from_letters(wordList, notIn):
    return [ele for ele in wordList if all(ch not in ele for ch in notIn)]


# this one works BUT NEED TO CHECK FOR DOUBLE
def only_with_green(wordList, pattern):
    if pattern == ["-", "-", "-", "-", "-"]:
        return wordList
    wordList = [word for word in wordList if all(p == "-" or p == w for w, p in zip(word, pattern))]
    return wordList


# this one works BUT NEED TO ACCOUNT FOR DOUBLE
def only_with_yellow(wordList, inside):
    for i in inside:
        wordList = [word for word in wordList if all(c in word for c in inside[i])]
        wordList = [word for word in wordList if not any(word[i-1] == c for c in inside[i])]
    return wordList
