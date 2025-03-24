package cs3500.pawnsboard.model;

/**
 * Represents the overall game model for Pawns Board.
 */
public interface IPawnsBoardModel {
  /**
   * Starts the game by initializing player hands and setting up
   * the initial game state.
   * GameState should be ONGOING.
   * Each side of the board should start with three pawns each.
   * Each player should have their hands of cards filled.
   * @throws IllegalStateException if the game has already started
   */
  void startGame();

  /**
   * Places a card on the board at the given coordinate.
   * @param x the row index
   * @param y the column index
   * @param card the given card to be placed
   * @throws IllegalArgumentException if the player doesn't have the card in hand
   * @throws IllegalStateException if the game hasn't started
   * @throws IllegalStateException if the game has already ended
   */
  void placeCard(int x, int y, ICard card);

  /**
   * Allows the current player to pass their turn.
   * If both players pass consecutively then the game ends.
   * @throws IllegalStateException if the game hasn't started
   * @throws IllegalStateException if the game has ended
   */
  void passTurn();

  /**
   * Gets the current state of the game.
   * @return the current GameState of the game.
   */
  GameState getGameState();

  /**
   * Returns the game board.
   * @return the game board.
   */
  IBoard getBoard();
}
