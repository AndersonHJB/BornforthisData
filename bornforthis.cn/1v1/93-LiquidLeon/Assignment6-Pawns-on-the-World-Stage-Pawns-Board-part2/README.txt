Overview
The Pawns Board Game is a strategic two player game where players use cards to gain control of a
board. Players can place cards in cells where they have pawns, and each card has an influence grid
that affects nearby cells. The game determines a winner based on the scores on each row.
The game is designed to support various board sizes and different sets of cards.

The code includes
- a model that represents the game logic, including the board, players, cards, and decks.
- a deck reader to generate cards from a configuration file
= a textual view to render the board state in textual form
- a main method to run a sample game

Some assumptions about the game is that the board is rectangular with an odd number of columns.
Players use separate decks, with the blue deck influence grid reversed when compared to the red deck
The game starts with three pawns per player spread out across the first and last column.
Players can only place cards in cells that they have pawns in. The number of pawns have to cover
the cost of the card, and the player has to own the pawns.

Key components:
Model:
PawnsBoardModelImpl: the main game logic implementation, manages turns, board updates, game state

DeckReader:
reades the deck configuration file and creates two separate decks
- red deck uses the influence grid in the file
- blue deck reverses the influence grid

View:
provides a textual visualization of the board


Key subcomponents:
Board: represents the grid where players place cards
Cell: a single square on the board, containing pawns or card
Player: represents a game participant with a hand and a deck
Card: represents a card with an influence grid, value, and cost
InfluenceGrid: a 5x5 grid that determines how a card influences the board when placed


Layout of the code

docs
- deck.config: Configuration file for the cards and decks
src
- model
    - ICard: interface for card
    - AbstractCard: abstract class for card
    - Card: implementation of card

    - IBoard: iterface for board
    - Board: implementation of baord

    - ICell: interface for cell
    - Cell: implementation of cell

    - IDeck: interface for deck
    - AbstractDeck: abstract class for deck
    - Deck: implementation of deck

    - ICard: interface for card
    - AbstractCard: abstract class for deck
    - Card: implementation of card

    - IInfluenceGrid: interface for influence grid
    - InfluenceGrid: implementation for influence grid

    - IPlayer: interface for player
    - AbstractPlayer: abstract class for player
    - Player: implementation of player

    - GameState: enum class for various game states

    - IPawnsBoardModel: interface for the game logic model
    - PawnsBoardModelImpl: implementation of game logic model

    - DeckReader: reader for deck configuration file

- view
    - ITextualView: interface for textual view
    - TextualPawnsBoardView: implementation of textual view

test
- model
    - PawnsBoardModelTest: test class for all classes and methods in the model package
- view
    - PawnsBoardViewTest: test class for all classes and methods in the view package


Future improvements
- implement AI players
- add a grpahical user interface
- extend to different board sizes and custom decks

User-Player interface design for Pawns Board Game
methods:
- startGame: initialize the game and sets up the board players and decks
- renderGameState: render the current board state
- getUserAction: asks the user for inputs (place card or pass turn)
- execute: executes the given move
- isValidMove(): checks if a move is legal according to the game logic
- isGameOver(): determine if the game is over and announces winner if it is

the interface basically needs to receive user input and execute the input onto the board, and
display the results.

