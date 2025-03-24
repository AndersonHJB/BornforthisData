package cs3500.pawnsboard.model;

import java.util.List;

/**
 * Represents a deck of Card cards in Pawn Board.
 */
public class Deck extends AbstractDeck {

  /**
   * Constrcuts a deck with the given cards.
   * @param cards A list of Card objects.
   */
  public Deck(List<ICard> cards) {
    super(cards);
  }
}
