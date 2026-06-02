"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in ["J", "Q", "K"]:
        return 10
    if card == "A":
        return 1
    return int(card)


def value_of_new(card):
    """Helper function where Ace values default to 11."""
    if card in ["J", "Q", "K"]:
        return 10
    if card == "A":
        return 11
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    
    if val1 > val2:
        return card_one
    if val2 > val1:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an ace card."""
    # If the hand already has an Ace, its value is calculated as 1 or 11 elsewhere.
    # We check if adding an 11 would bust the hand (go over 21).
    current_total = value_of_card(card_one) + value_of_card(card_two)
    
    if "A" in [card_one, card_two] or current_total + 11 > 21:
        return 1
    return 11


def is_blackjack(card_one, card_two):
    """Determine if a player has a blackjack hand."""
    return (value_of_new(card_one) + value_of_new(card_two)) == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    return (value_of_card(card_one) + value_of_card(card_two)) in {9, 10, 11}