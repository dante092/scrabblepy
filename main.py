import scrabble

""" Scrabblepy, a commandline utility that allows you to input scrabble letters, and receive a list of possible scored
 words by CmD_Override"""


words = scrabble.SrabblePy.load_words()
rack= scrabble.SrabblePy.load_rack()
space_avail = scrabble.SrabblePy.blank_spaces()
matches = scrabble.SrabblePy.word_generator(rack, words)
filtered_words = scrabble.SrabblePy.space_allowed_per_word(matches, space_avail)

score_words = scrabble.SrabblePy.score_words(filtered_words)
scrabble.SrabblePy.display_word(score_words)
