# Problem Set 2, hangman.py
# Name: Sophia
# Collaborators:
# Time spent: 

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

    


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded!")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

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
    secure_list = list(secret_word)
    string = ''
    for i in secure_list:
      if i in letters_guessed:
        string = string + i
      else:
        string = string + '_ '
    return string




def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    list_of_secure_word = list(secret_word)
    for i in list_of_secure_word:
      if i in letters_guessed:
        continue
      else:
        return False
    return True



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    n_guessed = ''
    for i in string.ascii_lowercase:
        if not i in letters_guessed:
            n_guessed += i
    return n_guessed
    
    

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
    number_of_guesses = 6
    number_of_attempts = 3
    print('You have', number_of_attempts, 'warnings left')
    list_of_available = []
    while True:
      print('---------------')
      if number_of_guesses <= 0:
            print('Sorry, you ran out of guesses. The word was "', secret_word, '"')
            break
      print("You have', number_of_guesses, 'guesses left")
      print("Available letters:", get_available_letters(list_of_available))
      str = input("Please guess a letter:").lower()
      if (not str.isalpha()):
        print("Ooops! That is not a valid letter.")
        if number_of_attempts == 0:
          number_of_guesses = number_of_guesses - 1
        else:
          number_of_attempts = number_of_attempts - 1
          print("You have", number_of_attempts, "warnings left")
      elif len(list(str)) != 1:
        print('Ooops! Enter one letter!')
        if num_of_warnings == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_warnings = num_of_warnings - 1
          print('You have', num_of_warnings, 'warnings left')
      elif ( not str in list ( get_available_letters ( list_of_available ) ) ):
        print("Ooops! You have already entered this letter!")
        if number_of_attempts == 0:
          number_of_guesses = number_of_guesses - 1
        else:
          number_of_attempts = number_of_attempts - 1
          print("You have",number_of_attempts, "warnings left")
      else:
        list_of_available.append(str)
        if str in list( secret_word ):
          print("Good guess:", is_word_guessed( secret_word, list_of_available ))
          print("Please guess a letter:", is_word_guessed( secret_word, list_of_available ))
        elif not str in list( secret_word ):
          print("Oops! That letter is not in my word.")
          number_of_guesses = number_of_guesses - 1
          print('Please guess a letter:', is_word_guessed( secret_word, list_of_available ))
        elif not str in list(secret_word) and str in ['a', 'e', 'i', 'o', 'u']:
              print('Oops! That letter is not in my word.')
              number_of_guesses = number_of_guesses - 2
        if get_guessed_word( secret_word, list_of_available ) == True:
          print('---------------')
          available = []
          for i in list(secret_word):
            if i in available:
              continue
            else:
              available.append(i)
          score = len(available)*number_of_guesses
          print('Congratulations, you won! \nYour total score for this game is:', score)
          break

def match_with_gaps(my_word = 'a_ ple', other_word = 'aople' ):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = ''.join(my_word.split())
    if len(other_word) == len(my_word):
        for i in my_word:
            if i != '_':
                my_word_split = my_word.split(i)
                other_word_split = other_word.split(i)
                if len(other_word_split) !=len(my_word_split):
                    return False
                else:
                    for v in range(len(my_word_split)):
                        if len(other_word_split[v]) !=len(my_word_split[v]):
                            return False
    else:
        return False
    return True





def show_possible_matches(my_word):
    global wordlist
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    for i in wordlist:
        if match_with_gaps(my_word, i):
            print(i, end='\n')
    print()


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    num_of_guesses = 6
    num_of_available = 3
    print('You have', num_of_available, 'warnings left')
    list_of_available = []
    while True:
      print('---------------')
      if num_of_guesses <= 0:
        print('Sorry, you ran out of guesses. The word was "', secret_word, '"')
        break
      print('You have', num_of_guesses, 'guesses left')
      print('Available letters:', get_available_letters(list_of_available))
      str = input('Please guess a letter: ').lower()
      if (str != '*' and not str.isalpha()):
        print('Ooops! Enter the letter.')
        if num_of_available == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_available = num_of_available - 1
          print('You have', num_of_available, 'warnings left')
      elif len(list(str)) != 1:
        print('Ooops! Enter one letter!')
        if num_of_available == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_available = num_of_available - 1
          print('You have', num_of_available, 'warnings left')
      elif (not str in list(get_available_letters(list_of_available)) and str != '*'):
        print('Ooops! You have already entered this letter!')
        if num_of_available == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_available = num_of_available - 1
          print('You have', num_of_available, 'warnings left')
      else:
        if str == '*':
          show_possible_matches(is_word_guessed(secret_word, list_of_available))
          continue
        list_of_available.append(str)
        if str in list(secret_word):
          print('Good guess:', is_word_guessed(secret_word, list_of_available))
        elif not str in list(secret_word):
          print('Oops! That letter is not in my word.')
          num_of_guesses = num_of_guesses - 1
          print('Please guess a letter:', is_word_guessed(secret_word, list_of_available))
        elif not str in list(secret_word) and str in ['a', 'e', 'i', 'o', 'u']:
          print('Oops! That letter is not in my word.')
          num_of_guesses = num_of_guesses - 2
          print('Please guess a letter:', is_word_guessed(secret_word, list_of_available))
        if get_guessed_word(secret_word, list_of_available) == True:
          print('---------------')
          available = []
          for i in list(secret_word):
            if i in available:
              continue
            else:
              available.append(i)
          total_score = num_of_guesses*len(available)
          print('Congratulations, you won! \nYour total score for this game is:', total_score)
          break
    





if __name__ == "__main__":
    pass

while True:
    n = input('Hello, do you want to play without prompts(1) or with?(2)\n')
    if n == '1' or n == '2':
        break
if n == 1:
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    print("\n")
else:
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    print("\n")