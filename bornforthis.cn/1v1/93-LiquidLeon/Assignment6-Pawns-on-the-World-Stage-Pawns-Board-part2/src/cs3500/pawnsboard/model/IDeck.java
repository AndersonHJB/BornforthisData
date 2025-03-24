package cs3500.pawnsboard.model;

/**
 * Represents a deck of cards in the game Pawns Board.
 */
public interface IDeck {
  /**
   * Draws the next card from the deck.
   * @return the drawn card, or null if the deck is empty.
   */
  ICard drawCard();

  /**
   * Gets the number of remaining cards in the deck.
   * @retrun The number of cards left in the deck.
   */
  int size();

}
