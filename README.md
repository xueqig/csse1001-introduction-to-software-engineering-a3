# UNO++
## 1 Introduction
This project follows a programming pattern called MVC (the Model, View, Controller) pattern.

## 2 Gameplay
Uno is a card based game consisting primarily of cards with both a colour and a number. Each player starts with a deck of seven cards. The player whose cards are visible is the starting player. Once the player makes a move by selecting their card to play, their cards will be hidden and it will move to the next players turn.

There are two piles in the middle of the board. The left pile is the pickup pile, a player should click this pile if they have no cards to play, it will add a card to their deck. The right pile is the putdown pile, a player has to pick a card from their deck which matches the card on top of the putdown pile.

The aim of the game is to have no cards left in your deck. Each turn a player can either select a card from their pile which matches the card on top of the putdown pile, or, they can pickup a new card from the pickup pile if they have no matching cards.

## 3 Files
* a2.py - main game logic 
* a2_support.py - contains supporting code and part of the controller 
* gui.py - contains the view 
* player.txt - a list of random player names to use for computer players 
* images/ - a directory of card images

## 4 Classes
### 4.1 Cards
A card represents a card in the uno game which has colour and number attributes. 

#### 4.1.1 Card
The basic type of colour and number.
Instances of Card should be initialized with Card(number, colour).

Methods in Card:
* get_number(self): Returns the card number 
* get_colour(self): Returns the card colour 
* set_number(self, number: int): Set the number value of the card 
* set_colour(self, colour: a2_support.CardColour): Set the colour of the card 
* get_pickup_amount(self): Returns the amount of cards the next player should pickup 
* matches(self, card: Card): Determines if the next card to be placed on the pile matches this card.
  * "Matches" is defined as being able to be placed on top of this card legally. 
  * A "match" for the base Card is a card of the same colour or number. 
* play(self, player: Player, game: a2_support.UnoGame): Perform a special card action. The base Card class has no special action.
* __str__(self): Returns the string representation of this card.
* __repr__(self): Same as __str__(self)

#### 4.1.2 SkipCard
A card which skips the turn of the next player. Matches with cards of the same colour.

#### 4.1.3 ReverseCard
A card which reverses the order of turns. Matches with cards of the same colour.

#### 4.1.4 Pickup2Card
A card which makes the next player pickup two cards. Matches with cards of the same colour

#### 4.1.5 Pickup4Card
A card which makes the next player pickup four cards. Matches with any card.

### 4.2 Deck
A collection of ordered Uno cards. A Deck should be initialized with Deck(starting_cards=None)
* get_cards(self): Returns a list of cards in the deck. 
* get_amount(self): Returns the amount of cards in a deck. 
* shuffle(self): Shuffle the order of the cards in the deck. 
* pick(self, amount: int=1): Take the first 'amount' of cards off the deck and return them. 
* add_card(self, card: Card): Place a card on top of the deck. 
* add_cards(self, cards: list<Card>): Place a list of cards on top of the deck. 
* top(self): Peaks at the card on top of the deck and returns it or None if the deck is empty.

### 4.3 Players
A player represents one of the players in a game of uno.

#### 4.3.1 Player
The base type of player which is not meant to be initiated (i.e. an abstract class).
The Player class should be initiated with Player(name) and implement the following methods:
* get_name(self): Returns the name of the player. 
* get_deck(self): Returns the players deck of cards. 
* is_playable(self): Returns True iff the players moves aren't automatic. 
* Raises a NotImplementedError on the base Player class. 
* has_won(self): Returns True iff the player has an empty deck and has therefore won. 
* pick_card(self, putdown_pile: Deck): Selects a card to play from the players current deck. 
  * Raises a NotImplementedError on the base Player class. 
  * Returns None for non-automated players or when a card cannot be played. 
  * If a card can be found, the card should be removed.

Each of the following classes should be a subclass of Player and should only alter methods required to implement the functionality as described.

#### 4.3.2 HumanPlayer
A human player that selects cards to play using the GUI.

#### 4.3.3 ComputerPlayer
A computer player that selects cards to play automatically.