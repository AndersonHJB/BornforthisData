package cs3500.pawnsboard.model;

import java.util.ArrayList;
import java.util.List;

/**
 * An abstract class for decks, providing base functionality.
 */
public class AbstractDeck implements IDeck {
  protected final List<ICard> cards;

  /**
   * Constructs a deck with a given list of cards.
   * @param cards A list of Card objects
   */
  public AbstractDeck(List<ICard> cards) {
    this.cards = new ArrayList<>(cards);
  }

  @Override
  public ICard drawCard() {
    if (!cards.isEmpty()) {
      return cards.remove(0);
    }
    return null;
  }

  @Override
  public int size() {
    return cards.size();
  }
}
