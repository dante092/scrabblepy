import scrabble

flag = str
while flag != 'EXIT':

    rack = scrabble.SrabblePy.create_rack()
    blankspaces = int(scrabble.SrabblePy.blank_spaces())
    matches = scrabble.SrabblePy.word_generator(rack)
    filtered_matches = scrabble.SrabblePy.space_allowed_per_word(matches, blankspaces)
    scrabble.Menu.display(filtered_matches)
    scrabble.SrabblePy.display_word(filtered_matches)

    flag = input('press Enter To Enter next rack')
    flag = flag.upper()

    scrabble.Menu.clear()





