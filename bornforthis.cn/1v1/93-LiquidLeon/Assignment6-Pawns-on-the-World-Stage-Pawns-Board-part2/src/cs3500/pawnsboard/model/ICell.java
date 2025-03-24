package cs3500.pawnsboard.model;

/**
 * Represents a single cell on the board in the game Pawns Board.
 * A cell can contain a card, a number of pawns (0 to 3), or be empty.
 * Pawns can belong to either player and may be influenced by placed cards.
 */
public interface ICell {

  /**
   * Checks if this cell is empty.
   * @return true if the cell is empty, false otherwise.
   */
  boolean isEmpty();

  /**
   * Checks if this cell contains a card.
   * @return true if a card is present, false otherwise.
   */
  boolean hasCard();

  /**
   * Checks if this cell contains any pawns.
   * @return true if pawns are present, false otherwise.
   */
  boolean hasPawns();

  /**
   * Gets the number of pawns in this cell.
   * @return the count of pawns in this cell.
   */
  int getPawnCount();

  /**
   * Retrieves the card in this cell.
   * @return the card in this cell.
   */
  ICard getCard();

  /**
   * Places a card in this cell, replacing existing pawns.
   * INVARIANT: each cell can only contain pawns, cards, or nothing.
   * INVARIANT: a cell with a card cannot have pawns.
   * @param card The card to  be placed in the cell.
   * @param isRed true if the red player placed the card, false otherwise
   * @throws IllegalStateException if a card is already in the cell.
   * @throws IllegalArgumentException if there aren't enough pawns to cover the cost.
   * @throws IllegalArgumentException if the pawns in this cell isn't owned by the player.
   */
  void placeCard(ICard card, boolean isRed);

  /**
   * Adds a give amount of pawns to this cell.
   * INVARIANT: a cell cannot contain more than 3 pawns.
   * @param count the number of pawns to add.
   * @throws IllegalArgumentException if the count is negative
   */
  void addPawns(int count, boolean isRed);

  /**
   * Switches who owns the pawns in this cell.
   */
  void switchPawnsOwnership();

  /**
   * Returns if the cell is owned by the red player.
   * @return true if the cell is owned by red player, false otherwise
   */
  boolean isOwnedByRed();
}
