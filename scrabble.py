import sys
import os


class Menu():
    """Creates a Menu Class, to draw Menu items througout the project  """

    def title():
        print('[S] [C] [R] [A] [B] [B] [L] [E] [P] [Y]'.center(70, '='))

    def display(filtered_matches):
        print('RESULTS'.center(65, '-'))
        print(str(len(filtered_matches)) + ' HITS')

    def clear():
        os.system('clear')


class SrabblePy():

    def load_words():
        Menu.title()
        f_open = open('sowpods.txt', 'r+')
        dictionary = f_open.readlines()
        dictionary_list = []
        print('\nLoading words...')
        for word in dictionary:
            dictionary_list.append(word.strip('\n'))
        print(str(len(dictionary_list))+' words loaded.')
        return dictionary_list

    def load_rack():
        """Creates a list of letters representing a scrabble rack """
        rack = input('\nRack: ')
        if rack.isalpha():
            rack = rack.upper()
            rack = list(rack)
            return rack

        else:
            print('Error: letters only')
            sys.exit()

    def blank_spaces():
        """creates the amount of spaces that a word can take up"""
        max_space = int(input('Space on board: '))
        return max_space

    def word_generator(rack, dictionary_list):
        """ Creates a list of words that can be created with the letters in rack"""
        matches = []
        print('\n')
        print('Analyzing words...')
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
        """Filters out words by length"""
        print('Filtering words by space...')
        availible_words = matches[:]
        for word in availible_words:
            if len(word) > space:
                availible_words.remove(word)
        return availible_words

    def display_word(matches):
        for word, score in matches.items():
            print('Word: - ' + word + " | Score: " + str(score))

    def score_words(matches):
        print('Scoring words...')
        print(str(len(matches)) + ' Words detected.')
        input('\nPress Enter to Display words\n')
        scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
              "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
              "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
              "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
              "X": 8, "Z": 10}
        scored_words={}

        for word in matches:
            score = 0
            for letter in word:
                score = score + scores[letter]
                scored_words[word]=score

        return scored_words

# ToDo List


# Function that allows you to choose specific placing for letters.
# Function that allows you change the amount of results you get.
