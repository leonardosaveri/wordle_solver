# wordle_solver
Python project to help solve the daily Wordle game (https://www.nytimes.com/games/wordle/index.html).

<i>Credit to Todd Wells (https://github.com/ttop) for the code to find the best starting word (https://github.com/ttop/wordle_starting_guess).<br></i>
I rearranged his code to find the best word every time I reduce the list of accepted words.

### This repository contains:
<ul>
  <li><b>WordList.txt:</b> a text file containing all the words <i>(both accepted and possible)</i> that I downloaded from the Worlde source code. I put them in a single list and alphabetically ordered them to don't spoil the solution.</li>
  <li><b>PossibleWordList.txt:</b> a text file containing only the possible solutions.</li>
  <li><b>wordleSolver.py:</b> which contains the main code.</li>
  <li><b>scoringWord.py:</b> which, given a list of words, returns the best word to try out of the list <i>(using the code from Todd Wells)</i>.</li>
  <li><b>inputTry.py:</b> which, given the yellow and green letters, reduces the word list to only the possible solutions.</li>
</ul>

### How to use
If you run <b>wordleSolver.py,</b> the program will suggest the best word to try out of the list of words <i>(you can either use the WordList.txt or the PossibleWordList.txt file).</i> In the case of my list, which contains <b>both</b> possible and accepted words, it returns the word <b>tares</b> <i>(while, if we use only the possible answers list, returns <b>slate</b>).</i><br>
Then the program asks what word you choose to enter <i>(this is because one could prefer to insert a different word than the one suggested).</i><br>
At this point, the program asks you to enter the solution that wordle gives you. To facilitate the usage, I decided to use '<b>-</b>' for the letters that are not present, lowercase letters for the "yellow letters" and uppercase letters for the "green letters."<br>
At this point the program tells us the letters that cannot be <i>(where was a '<b>-</b>' put)</i> and tells us how many are the possible words remaining and suggesting the next best guess, finally asking the user to input the new chosen word.<br>
When you find the solution, you can enter the final word so that the program ends.<br>


### Statistics
When running this program through another program that I wrote to test how many tries it takes to reach each word in the list based on this code, I got this averages:
<ul>
  <li><b>For the WordList.txt list:</b> 4.6934424963312 tries.</li>
  <li><b>For the PosibleWordList.txt list:</b> 3.60691144708423 tries.</li>
</ul>
We can see that using only the possible solutions the average tries is much lower, but I feel it's like cheating since a human would try all the accepted and possible words.


### What to work on
I still have to account for words with double or triple letters and I also believe that the code to remove words from the list based on certain characteristics could be made also more efficient.<br>
<b>The next step</b> is to create my word scoring script.
