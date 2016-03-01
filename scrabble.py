""" Scrabblepy, a commandline utility that allows you to input scrabble letters, and receive a list of possible scored words by CmD_Override"""

class ScrabblePy():
    """ Unnecessary class. For learning purpose """
    def __init__(self):
        self.dictionary = self.load_words()

    def run(self):
        """ Mainloop """
        print('[S] [C] [R] [A] [B] [B] [L] [E] [P] [Y]'.center(70, '='))
        print('{} words loaded.'.format(len(self.dictionary)))
        while True:
            rack = self.load_rack()
            spaces = self.blank_spaces()
            words = self.word_generator(rack, spaces)
            print('Scoring words...')
            print('{} Words detected.'.format(len(words)))
            score = self.score_words(words)
            self.display_word(score)
            prompt = input('\nOnce more? [y]/n ')
            if prompt and prompt != 'y':
                break

    def load_words(self, file='sowpods.txt'):
        """
        Opens the dictionary file and creates a list of possible words.
        """
        with open(file, 'r') as f:
            return [word.strip() for word in f]

    def load_rack(self):
        """Creates a list of letters representing a scrabble rack """
        while True:
            rack = input('\nRack: ')
            if rack.isalpha():
                return list(rack.upper())
            print('Error: letters only')

    def blank_spaces(self):
        """creates the amount of spaces that a word can take up"""
        max_space = int(input('Space on board: '))
        return max_space

    def word_generator(self, rack, spaces):
        """ Creates a list of words that can be created with the letters in rack"""
        def contains(word1, word2):
            if set(word1).difference(set(word2)):
                return False
            for letter in set(word1):
                if word1.count(letter) > word2.count(letter):
                    return False
            return True

        return [word for word in self.dictionary
                if len(word) <= spaces and contains(word, rack)]

    def display_word(self, matches):
        """
        Displays Each word and is score.
        """
        for word, score in sorted(matches.items(), key=lambda pair: pair[1]):
            print('Word: - ' + word + " | Score: " + str(score))

    def score_words(self, matches):
        """
        Scores each word.
        """
        input('\nPress Enter to Display words\n')
        scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
              "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
              "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
              "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
              "X": 8, "Z": 10}
        
        scored_words={}
        for word in matches:
            scored_words[word] = sum(scores[letter] for letter in word)
        return scored_words

if __name__ == '__main__':
    ScrabblePy().run()

# ToDo List
# Function that allows you to choose specific placing for letters.
# Function that allows you change the amount of results you get.
