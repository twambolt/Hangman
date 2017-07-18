import random
import sys
# pylint: disable=missing-docstring

"""
a Puzzle represents a puzzle object
a word is a string representing the word to be guessed
a puzzle is a list representing the letters of the puzzle still needed to be guessed
a tries is an int representing the amount of tries left in a puzzle
"""


class Puzzle:

    def __init__(self, word, pboard, tries=10, guesses =[], completed=False):
        self.word = word
        self.pboard = pboard
        self.tries = tries
        self.guesses = guesses
        self.completed = completed

    def __eq__(self, other):
        return (type(other) == Puzzle
                and self.word == other.word
                and self.pboard == other.pboard
                and self.tries == other.tries
                and self.guesses == other.guesses
                and self.completed == other.completed
                )

    def __repr__(self):
        return "\n\n\n\n%r, %r tries left, \n\nletters guessed = %r" % (self.pboard, self.tries, self.guesses)


def main():

    word = get_word()
    puzzle = Puzzle(word, ['-'] * len(word))
    while puzzle.completed == False:
        print(puzzle)
        puzzle = update_puzzle(puzzle)
        if puzzle.tries <= 0:
            print ('\n\n\n%r\n\n\n'  % (word))          
            print("\n\nGAME OVER!\n\n")
            exit()
        
    print(puzzle)
    print ('\n\n\n%r\n\n\n'  % (word))
    print('\n\nYOU WIN!\n\n')
    exit()




def get_word():
    """
    None -> string

    receieves a word from a user for another user to
    guess in a two player sort of mode the word needs
    to be at least 5 characters long and contain no
    special characters
    """

    word_list = load_words('game_words.txt')
    word = word_list[random.randint(0, 248433)].upper()
    return word

def update_puzzle(puzzle):
    """
    Puzzle -> Puzzle

    updates the puzzle after recieving a guess
    """
    word_list = list(puzzle.word)
    guess = str((input('\nGuess a letter: '))).upper()
    while guess in puzzle.guesses or len(guess) > 1:
        print('\nError: Invalid guess\n')
        guess = str((input('Guess a letter: '))).upper()
    puzzle.guesses.append(guess)
    match_list = []
    for i in range(len(word_list)):
        if guess == word_list[i]:
            match_list.append(i)
    if len(match_list) == 0:
        puzzle.tries -= 1
        return puzzle
    for num in match_list:
        puzzle.pboard[num] = word_list[num]
    if '-' not in puzzle.pboard:
        puzzle.completed = True
    return puzzle


def load_words(file):
    '''
    file -> List (array)

    places the words in 'game_words.txt' into
    an array based list for the program to 
    later randomly choose from

    '''

    inFile = open(file, 'r')
    word_list = []
    for word in inFile:
        word_list.append(word.strip('\n'))
    return word_list







if __name__ == '__main__':
    main()


