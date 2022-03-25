#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random


__author__ = "Xueqi Guan & 44176628"

class Player:
    """
    A player represents one of the players in Uno game which has name attribute.
    """
    def __init__(self, name):
        """
        Constructs a player in Uno game.

        Parameters:
            name (str): name of the player.
        """
        self._name = name
        self._deck = Deck()

    def get_name(self):
        """(str) Returns the name of the player."""
        return self._name
    
    def get_deck(self):
        """(Deck) Returns the players deck of cards."""
        return self._deck

    def is_playable(self):
        """Raises a NotImplementedError on the base Player class."""
        raise NotImplementedError ("is_playable to be implemented by subclasses")

    def has_won(self):
        """
        (bool) Returns True iff the player has an empty deck and has won.
        """
        return self.get_deck().get_amount() == 0

    def pick_card(self, putdown_pile):
        """
        Raises a NotImplementedError on the base Player class.

        Parameters:
            putdown_pile (Deck): a deck which contains the cards has been played
        """
        raise NotImplementedError ("pick_card to be implemented by subclasses")
        
class HumanPlayer(Player):
    def is_playable(self):
        """(bool) Returns True iff the players moves are not automatic."""
        return True

    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.

        Parameters:
            putdown_pile (Deck): a deck which contains cards has been played

        Returns:
            None
        """
        return None

class ComputerPlayer(Player):
    def is_playable(self):
        """(bool) Returns False iff the players moves are automatic."""
        return False

    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.

        Parameters：
            putdown_pile (Deck): a deck which contains cards has been played

        Returns:
            (Card): card being played or None if no card is found.
        """
        for card in self.get_deck().get_cards():
            if card.matches(putdown_pile.top()):
                self.get_deck().get_cards().remove(card)
                return card
        return None


class Deck:
    """
    A deck is a collection of ordered Uno cards.
    """
    def __init__(self, starting_cards = None):
        """
        Constructs a deck in Uno game.

        Parameters:
            starting_cards (list): a list of the starting cards.
        """
        self.starting_cards = starting_cards
        # Check if starting_cards is None
            # Assign a new empty list to self.starting_cards
        if self.starting_cards == None:
            self.starting_cards = []

    def get_cards(self):
        """(list) Returns a list of cards in the deck."""
        return self.starting_cards

    def get_amount(self):
        """(int) Returns the amount of cards in the deck."""
        return len(self.starting_cards)

    def shuffle(self):
        """Shuffles the order of the cards in the deck."""
        random.shuffle(self.starting_cards)

    def pick(self, amount = 1):
        """
        Takes the first 'amount' of cards off the deck and return them.

        Parameters:
            amount (int): the amount of cards being taken.

        Returns:
            (list): cards being taken.
        """
        picked_card = self.starting_cards[len(self.starting_cards) - amount:]
        # Remove the last amount of cards in starting_cards
        del self.starting_cards[len(self.starting_cards) - amount:]
        return picked_card

    def add_card(self, card):
        """
        Places a card on top of the deck.

        Parameters:
            card (Card): the card being placed on top of the deck.
        """
        self.starting_cards.append(card)

    def add_cards(self, cards):
        """
        Places cards on top of the deck.

        Parameters:
            cards (Card): the cards being placed on top of the deck.
        """
        self.starting_cards.extend(cards)

    def top(self):
        """
        Peaks at the card on top of the deck.

        Returns:
            (Card): the top card of deck or None if the deck is empty.
        """
        if self.starting_cards == []:
            return None
        else:
            return self.starting_cards[-1]


class Card:
    """
    A card represents a card in the Uno game which has colour and number attributes.
    """
    def __init__(self, number, colour):
        """
        Constructs a card in Uno game
        
        Parameters:
            number (int): the number in the card.
            colour (str): the colour of the card.
        """
        self._number = number
        self._colour = colour

    def get_number(self):
        """(int) Returns the card number."""
        return self._number

    def get_colour(self):
        """(CardColour) Returns the card colour."""
        return self._colour

    def set_number(self, number):
        """
        Sets the number value of the card.
        
        Parameters:
            number (int): the number being assigned to the card.
        """
        self._number = number

    def set_colour(self, colour):
        """
        Sets the colour of the card.
        
        Parameters:
            colour (CardColour): the colour being assigned to the card.
        """
        self._colour = colour

    def get_pickup_amount(self):
        """Returns the amount of cards the next player should pick up."""
        return 0
        
    def matches(self, card):
        """
        Determines if the next card to be placed on the pile matches base card.

        Parameters:
            card (Card): the card being matched with.

        Returns:
            (bool): True if the card has same colour or number as base card.
        """
        return self._number == card.get_number() or self._colour == card.get_colour()

    def play(self, player, game):
        """
        The base Card class has no special action.

        Parameters:
            player (Player): a player in Uno game.
            game (UnoGame): the game of Uno.
        """
        pass

    def __str__(self):
        """Returns the string representation of the card."""
        return repr(self)

    def __repr__(self):
        """Returns the string representation of the card."""
        return "{0}({1}, {2})".format(self.__class__.__name__, self._number, self._colour)

class SkipCard(Card):
    def matches(self, card):
        """
        Determines if the next card to be placed on the pile matches base card.

        Parameters:
            card (Card): the card being matched with.

        Returns:
            (bool): True if the card has same colour as base card.
        """
        return self._colour == card.get_colour()

    def play(self, player, game):
        """Skips the turn of the next player."""
        game.skip()

class ReverseCard(Card):
    def matches(self, card):
        """
        Determines if the next card to be placed on the pile matches base card.

        Parameters:
            card (Card): the card being matched with.

        Returns:
            (bool): True if the card has same colour as base card.
        """
        return self._colour == card.get_colour()
    
    def play(self, player, game):
        """Transfers the turn back to the previous player and reverses the order."""
        game.reverse()

class Pickup2Card(Card):
    def get_pickup_amount(self):
        """Returns the amount of cards the next player should pick up."""
        return 2
    
    def matches(self, card):
        """
        Determines if the next card to be placed on the pile matches base card.

        Parameters:
            card (Card): the card being matched with.

        Returns:
            (bool): True if the card has same colour as base card.
        """
        return self._colour == card.get_colour()

    def play(self, player, game):
        """The next player picks two cards."""
        two_cards = game.pickup_pile.pick(2)
        game.get_turns().peak().get_deck().add_cards(two_cards)

class Pickup4Card(Card):
    def get_pickup_amount(self):
        """Returns the amount of cards the next player should pick up."""
        return 4

    def matches(self, card):
        """
        Determines if the next card to be placed on the pile matches base card.

        Parameters:
            card (Card): the card being matched with.

        Returns:
            (bool): True as Pickup4Card matches with any card.
        """
        return True
    
    def play(self, player, game):
        """The next player picks four cards."""
        four_cards = game.pickup_pile.pick(4)
        game.get_turns().peak().get_deck().add_cards(four_cards)

def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
