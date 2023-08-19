from deck import Card

def faceUpCards(cards, return_string=True):
    """
    Instead of a boring text version of the card we render an ASCII image of the card.
    :param cards: One or more card objects
    :param return_string: By default we return the string version of the card, but the dealer hide the 1st card and we
    keep it as a list so that the dealer can add a hidden card in front of the list
    """
    # create an empty list of list, each sublist is a line
    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        # "King" should be "K" and "10" should still be "10"
        if card.get_value() == '10':  # ten is the only one who's value is 2 char long, adjust spacing
            value = card.get_value()
            space = ''  # double card value (10), no blank space
        else:
            value = card.get_value()[0]  # access first index of string for abbreviation ('K' from 'King')
            space = ' '  # single card value, use a blank space to will the void
        
        suit = card.get_suit()  # get the cards suit

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(value, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, value))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    # hidden cards do not use string
    if return_string:
        return '\n'.join(result)
    else:
        return result
    

def halfFaceUpCards(cards, return_string=True):
    """
    Similar to faceUpCards(), but only shows half of the card. Useful for showing multiple cards if 
    player/dealer hits.
    """
    lines = [[] for i in range(5)]

    for index, card in enumerate(cards):
        if card.get_value() == '10': 
            value = card.get_value()
            space = '' 
        else:
            value = card.get_value()[0]
            space = ' '
    
        suit = card.get_suit()

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(value, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    if return_string:
        return '\n'.join(result)
    else:
        return result


def dealerCards(cards):
    """
    Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
    :param cards: A list of card objects, the first will be hidden
    :return: A string, the nice ascii version of cards
    """
    # a flipper over card. # This is a list of lists instead of a list of string becuase appending to a list is better then adding a string
    lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    # store the non-flipped over card after the one that is flipped over
    cards_except_first = faceUpCards(cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    # make each line into a single list
    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    # convert the list into a single string
    return '\n'.join(lines)
