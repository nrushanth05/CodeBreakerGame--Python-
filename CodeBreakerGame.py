"""
Name: Nrushanth Stuahahran
Description: Codebreaker game
Date: Jan 24, 2022
"""

## Codebreaker Game - Practice with Lists, print, variables, functions, loops

import random

def create_code(characters, length):
    """
    Return a new random code that is 'length' characters long and contains only \
    the characters in 'character'
    
    create_code(VALID_CHARS,SIZE)
    >>> ['R','Y','I','V','G']
    create_code(VLID_CHARS,SIZE)
    >>> 
    """
    # empty variable to store code
    list_code = []
    #for each letter in code
    for i in range(length):
        #adds a random letter from VALID_CHARS
        list_code.append(random.choice(characters))
    
    return list_code

def find_fully_correct(answer, guess):
    """
    Return's number of correctly placed colours based on answer and guess
    
    >>>find_fully_correct(['Y','G','G','P','R'],['Y','G','G','P','R'])
    ['b','b','b','b','b']
    
    >>> find_fully_correct(['Y','G','G','P','R'],['O','R','G','B','B'])
    ['b']
    """
    # list stores fully correct clues
    fully_correct_clue = []
    # for each letter in guess
    for i in range(len(answer)):
        #adds "b" to fully_correct_clue if both value and index match
        if guess[i] == answer[i]:
            fully_correct_clue.append("b")
    return fully_correct_clue

def remove_fully_correct(list1,list2):
    """
    Return guess but with fully correct colours matching in answer removed
    
    >>> remove_fully_correct(['A','B','C','D','E'],['A','B','C','E','D'])
    ['E','D']
    >>> remove_fully_correct(['F','A','D','E','N'],['N','F','A','D','E'])
    ['N','F','A','D','E']
    """
    # variable to be used
    answer = list1
    # converts list to string to avoid errors during .remove()
    fully_correct = "".join(list2)
    # final list which will be returned with fully correct removed
    fully_correct_removed = list2
    # for every character in guess
    for i in range(len(answer)):
        # if both value and index match, that value is removed from \
        #fully_corrrect_removed    
        if list(fully_correct)[i] == answer[i]:
            fully_correct_removed.remove(answer[i])

    return fully_correct_removed
    

def find_colour_correct(answer, guess):
    """
    Return number of 'w's for partially correct colours in answer based on \
    guess
    >>> find_colour_correct(['G','I','V','B','O'],['O','G','I','V','B'])
    ['w','w','w','w','w']
    >>> find_colour correct(['G','I','V','B','O'],['G','O','P','R','I'])
    ['w','w']
    """
    # if there is a "2" version of a variable, it is because the prior \
    #variable changed the value of a variable throughout the entire program \
    #leading to various errors
    guess2 = "".join(guess)
    answer2 = "".join(answer)
    #These random print statements were used in the debugging proccess
    
    # get list of fully correct colours removed from guess
    fully_correct_removed = remove_fully_correct(list(answer2),list(guess2))
    # get list of fully correct colours removed from answer
    fully_correct_remaining = remove_fully_correct(list(guess2),list(answer2))
    
    
    # variable store partially correct clues
    partially_correct_clue = []
    
    count = 0
    for i in range(len(fully_correct_removed)):
        # checks if letter in guess is in answer
        if fully_correct_removed[i] in fully_correct_remaining:
          # if there is more colours in guess than their is in answer, should \
          #only add 1-(the amount of colours in guess)
          if fully_correct_removed.count(fully_correct_removed[i]) > fully_correct_remaining.count(fully_correct_removed[i]) and count < fully_correct_remaining.count(fully_correct_removed[i]):
            # used to count how many times the colour has been registered
            count += 1 
            #add "w"
            partially_correct_clue.append("w")
          # if there is less than or equal numbers of the colour in guess and \
          #answer, then register "w" for everytime of that colour's appearance
          elif fully_correct_removed.count(fully_correct_removed[i]) <= fully_correct_remaining.count(fully_correct_removed[i]):
            partially_correct_clue.append("w")
    return partially_correct_clue
        
def display_game(guesses, clues):
    """
    Given two lists of lists, print to the display each guess
    separated by a tab and the clues for that guess.
    
    """
    #stores the final output
    #creates "Guess" and "Clues" two tabs apart with 25 *'s beneath
    
    s = 'Guess\t\tClues\n' + '*' * 25 + '\n'
    for i in range(len(guesses)):
        for j in range(len(guesses[i])):
            # adds the guess according to their tuple index
            s = s + guesses[i][j] + ' '
        # adds a space for upcomming clues
        s = s + '\t'
        for k in range(len(clues[i])):
            # adds every character in clues according to their tuple index
            s = s + clues[i][k] + ' '
        # adds a new line for the next row of guess and clue
        s = s + '\n'
    return s

def valid(user_guess, valid_characters, guess_size):
    """
    Return True if user_guess only has characters from valid_characters and \
    is correct length
    
    >>>valid("GYPOG",VALID_CHARS,SIZE)
    True
    >>> valid("QRSTJKFGD", VALID_CHARS, SIZE)
    False
    """
    #checks if the length of guess matches guess_size
    if len(user_guess) == guess_size:
        # counter to help check if letter is in valid_characters
        count = 0
        #checks each letter
        for i in range(guess_size):
            # checks if each letter is in valid_characters
            if user_guess[i] in valid_characters:
                # adds one to the counter
                count += 1
        # if counter is equal to guess_size, all of the letters are in \
        # valid characters thus returns True
        if count == guess_size:
            return True
        # if counter is not equal to guess_size, some of the letters are not in \
        # valid characters thus returns False
        else:
            return False
    else:
        return False
if __name__ == '__main__':
    
    # the number of pegs in the answer
    SIZE = 5
    # the number of guesses the user gets
    TRIES = 15
    # the letters allowed representing the colours
    # red, orange, yellow, green, blue, indigo, violet
    VALID_CHARS = 'ROYGBIV'
    
    # fill in the rest... 
yes_no = "yes"
while yes_no == "yes":
    # uses create_code() to create a code based on VALID_CHARS and SIZE
    answer = create_code(VALID_CHARS,SIZE)
    # this was a constant for answer used to fix syntax and logical errors by \
    #allowing me to think of verious scenarios which otherwise could not have been\
    #done on randomly changing answers
    #answer = ['P', 'G', 'V', 'B', 'P']
    
    #empty list used to store guesses
    guesses = []
    #empty list used to store clues
    clues = []
    #repeats 15 times
    for i in range(TRIES):
        try_number = i
        #asks for and converts user_guess to list
        user_guess = list(input("\nPlease enter your guess of length " + str(SIZE) + " using the letters" + "("+ VALID_CHARS + "): "))
        
        #following print statements like these were used in the debugging process
        
        
        # if guess was correct, break the loop
        if user_guess ==  answer:
            break
        else:
            # repeats question until user inputs valid guess (does not consume tries)
            while valid(user_guess,VALID_CHARS,SIZE) == False:
                user_guess = list(input("\nPlease enter your guess again of length " + str(SIZE) + " using the letters "  + "("+ VALID_CHARS + "):"))
            
            guesses2 = "".join(user_guess) 
            #creates list of guesses
            guesses.append(user_guess)
            # appends fully correct clues to clues
            clues.append(find_fully_correct(answer,user_guess))
            # appends partially correct clues to clues in the same tuple index
            clues[i] = clues[i] + find_colour_correct(answer,user_guess)
            
            # due to logical errors, converting between list and str had to be done\
            #without impacting the rest of the program
            guesses[i] = list(guesses2)
            
            # display game
            print(display_game(guesses,clues))
            
            
    #at end of tries or correct guess        
    # if the user guess and answer are the same, print congrats
    if user_guess == answer:
      print("\nCongratulations! It took you " + str(try_number) + " guesses to find the code.")
      # ask if user wants to play again
      yes_no = input("\nWould you like to try again (yes/no): ")
    #if user guess and answer not same, print fail
    else:  
      print("\nI'm sorry you lose. The correct code was: " + "".join(answer))
       # ask if user wants to play again
      yes_no = input("\nWould you like to try again (yes/no): ")