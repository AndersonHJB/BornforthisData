package cs3500.pawnsboard.model;

/**
 * Represents a card in the game Pawns Board.
 */
public interface ICard {

  /**
   * Returns the name of the card.
   * @return the name of the card.
   */
  String getName();

  /**
   * Returns the cost of the card.
   * @return the cost of the card.
   */
  int getCost();

  /**
   * Returns the value of the card.
   * @return the value of the card.
   */
  int getValue();

  /**
   * Returns the influence grid of the card.
   * @return the influence grid of the card.
   */
  IInfluenceGrid getInfluenceGrid();

  /**
   * Checks if this card is equal to given card.
   * @param other the given ICard
   * @return true if they are the same, false otherwise.
   */
  boolean equals(Object other);

}
