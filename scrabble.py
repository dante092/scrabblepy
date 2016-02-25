import sys
import os


class Menu:
    """Creates a Menu Class, to draw Menu items througout the project  """
    def toolbar():
        """Prints menu of options"""
        print('''               | [DONE] [EXIT] [BLANK] | [HELP] | ''')

    def title():
        print('S C R A B B L E P Y'.center(65, '-'))
        Menu.toolbar()
        print("________________________________________________________________\n")

    def display(filtered_matches):
        print('RESULTS'.center(65, '-'))
        print(str(len(filtered_matches)) + ' HITS')

    def clear():
        os.system('clear')


class SrabblePy:
    def create_rack():
        """Creates a list of letters representing a scrabble rack """
        rack = []
        blank = ['a-Z']
        Menu.title()

        while True:
            tile = input('- ')
            tile = tile.upper()

            if tile.isalpha() == False:
                print('Numbers, spaces & Symbols are not allowed.')
                continue
            if tile == 'DONE':
                return rack

            if tile == 'BLANK':
                rack.append(blank)
                continue

            if tile == 'EXIT':
                sys.exit()

            if len(tile) > 1:
                print('Only one letter at a time is permitted.')
                continue

            rack.append(tile)

    def blank_spaces():
        """creates the amount of spaces that a word can take up"""
        max_space = input('How much space do you have on board: ')
        return max_space

    def word_generator(rack):
        """ Creates a list of words that can be created with the letters in rack"""
        matches = []
        f_open = open('sowpods.txt', 'r+')
        dictionary = f_open.readlines()
        dictionary_list = []

        for word in dictionary:
             dictionary_list.append(word.strip('\n'))

        for word in dictionary_list:
            availible_letters = rack[:]
            hits= 0
            for letter in word:
                if letter in availible_letters:
                    availible_letters.remove(letter)
                    hits += 1

                if len(availible_letters) >= 0 and len(word)==hits :
                    matches.append(word)

        return matches

    def space_allowed_per_word(matches, space):
        """Filters out words by length
        :param space:
        """
        availible_words = matches[:]
        for word in availible_words:
            if len(word) > space:
                availible_words.remove(word)
        return availible_words

    def display_word(matches):
        for word in matches: 
            print(" - " + word)
            
    def score_words(matches):
        scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
             "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
             "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
             "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, 
             "X": 8, "Z": 10} 

        for word in matches:
            word_score = 0 
            for letter in word:
                word_score = word_score + scores[letter]
                
     


# ToDo List



# Functions that scores each word.
# Function that displays each word in order of score H to L.
# Function that allows you change the amount of results you get.
