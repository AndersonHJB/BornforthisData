package cs3500.pawnsboard.model;

import java.util.List;

/**
 * Represents a player in Pawns Board.
 */
public interface IPlayer {
  /**
   * Gets the player's deck.
   * @return the player's deck.
   */
  IDeck getDeck();

  /**
   * Gets the player's current hand.
   * @return A list of cards in the player's hand.
   */
  List<ICard> getHand();

  /**
   * Draws a card from the players' deck.
   */
  void drawCard();

  /**
   * Discards a card after the player have placed it.
   */
  void removeCard(ICard card);
}
