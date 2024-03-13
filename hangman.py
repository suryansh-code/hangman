import random
import string

WORDLIST_FILENAME = "words.txt"

GUESS_LIMIT = 6
TOTAL_WARNINGS = 3


def countDis(str):

    s = set(str)
    return len(s)


def is_guessed(secret_word, guess_word, guess):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    
    secret_word_list = list(secret_word)
    blank_word = ""
    complete = 0

    while guess > 0:
        print(f"you have {guess} guesses left .")
        for char in secret_word:
            if char in guess_word:
                print("GUESS RIGHT")
                print(char, end=""),

            else:
                print("_", end=""),
                complete += 1

        if complete == 0:
            print("YOU WON")
            break


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = str()
    for char in secret_word:
        for letter in letters_guessed:
            if char == letter:
                guess += char
            else:
                continue

    if guess == secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed_word = ""
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += "_"
    return guessed_word



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    all_str = list(string.ascii_lowercase)
    for x in all_str:
        if x in letters_guessed:
            all_str.remove(x)
    return "".join(all_str)


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_no_gap = my_word.replace(" " , "")
    same_char = []
    blank_char = []
    if len(word_no_gap) == len(other_word):
        for index , letter in enumerate(word_no_gap):
            if letter in string.ascii_lowercase:
                same_char.append(index)
            else:
                blank_char.append(index)
    else:
        return False
    
    my_word_it = ''
    other_word_it = ''

    for index_same in same_char:
        for index_diff in blank_char:
            if other_word[index_diff] == word_no_gap[index_same]:
                return False
            my_word_it += word_no_gap[index_same]
            other_word_it += other_word[index_same]

    var = bool(my_word_it == other_word_it)
    return var


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    """
    possible_letter = []
    for i in wordlist:
        if match_with_gaps(my_word , i):
            possible_letter.append(i)

    hint_word = ' '.join(possible_letter)

    return hint_word

def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """

    guesses_remaining = GUESS_LIMIT
    warnings_remaining = 3
    good_guess = 0
    guesses_combine = []
    print(secret_word)

    score_distinct_letter = countDis(secret_word)

    while not is_word_guessed(secret_word, guesses_combine) and guesses_remaining > 0:
        failed = 0
        print(f"you have {guesses_remaining} guesses left")
        print(f"avaiable letters {get_available_letters(guesses_combine)}")
        guess_word = input("please guess a letter ").lower()
        print("__________________________________________")

        if guess_word == '*':
            print("possible matches are : " ,
                  show_possible_matches(get_guessed_word(secret_word,guesses_combine)))

        if not guess_word or guess_word not in string.ascii_lowercase:
            if warnings_remaining != 0:
                warnings_remaining -= 1
                print(f"That is not a valid letter. You have {warnings_remaining} warning left.")

            else:
                print(
                    "That is not a valid letter."
                    "You have no warning left, so you lose one guess."
                )
                guesses_remaining -= 1

        elif guess_word in guesses_combine:
            if warnings_remaining != 0:
                warnings_remaining -= 1
                print(
                    "You've already guessed that letter. You have %d warning left."
                    % warnings_remaining
                )
            else:
                print(
                    "You've already guessed that letter. "
                    "You have no warning left, so you lose one guess."
                )
                guesses_remaining -= 1

        else:
            guesses_combine.append(guess_word)
            print(get_guessed_word(secret_word, guesses_combine))
            if guess_word not in secret_word:
                print("That letter is not in my word.")
                if guess_word in "aiueo":
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
            else:
                print("Good guess!")
                good_guess += 1

        if is_word_guessed(secret_word, guesses_combine):
            print("Congratulations, you won!")
            print(f"Your total score for this game is {good_guess * guesses_remaining}.")


        if guesses_remaining == 0:
            print("Sorry, you ran out of guesses. The word was %s." % secret_word)


def hangman_with_hints(secret_word):
        
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining = GUESS_LIMIT
    warnings_remaining = 3
    good_guess = 0
    guesses_combine = list()
    print(secret_word)


    while not is_word_guessed(secret_word, guesses_combine) and guesses_remaining > 0:
        print(f"you have {guesses_remaining} guesses left")
        print(f"avaiable letters {get_available_letters(guesses_combine)}")
        guess_word = input("please guess a letter ").lower()
        print("__________________________________________")
        print("__________________________________________")
        print("__________________________________________")

        if guess_word == '*':
            print("possible matches are : " ,
                  show_possible_matches(get_guessed_word(secret_word,guesses_combine)))

        if not guess_word or guess_word not in string.ascii_lowercase:
            if warnings_remaining != 0:
                warnings_remaining -= 1
                print(f"That is not a valid letter. You have {warnings_remaining} warning left.")

            else:
                print(
                    "That is not a valid letter. "
                    "You have no warning left, so you lose one guess."
                )
                guesses_remaining -= 1

        elif guess_word in guesses_combine:
            if warnings_remaining != 0:
                warnings_remaining -= 1
                print(f"You've already guessed that letter."
                      "You have {warnings_remaining} warning left.")

            else:
                print(
                    "You've already guessed that letter."
                    "You have no warning left, so you lose one guess."
                )
                guesses_remaining -= 1

        else:
            guesses_combine.append(guess_word)
            print(get_guessed_word(secret_word, guesses_combine))
            if guess_word not in secret_word:
                print("That letter is not in my word.")
                if guess_word in "aiueo":
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
            else:
                print("Good guess!")
                good_guess += 1

        if is_word_guessed(secret_word, guesses_combine):
            print("Congratulations, you won!")
            print(
                f"Your total score for this game is {good_guess * guesses_remaining}."
            )

        if guesses_remaining == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}. ")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.


    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.
    SECRET_WORDS = choose_word(wordlist)
    hangman_with_hints(SECRET_WORDS)
