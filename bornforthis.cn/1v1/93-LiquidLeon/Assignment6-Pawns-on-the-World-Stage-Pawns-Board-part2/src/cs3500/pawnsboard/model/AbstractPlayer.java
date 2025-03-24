package cs3500.pawnsboard.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Abstract representation of a player in the game.
 */
public class AbstractPlayer implements IPlayer {
  protected final String name;
  protected final IDeck deck;
  protected final List<ICard> hand;

  /**
   * Constructs a player with the given name, deck, and hand size.
   * INVARIANT: starting size of hand cannot be greater than a third of the deck size.
   * @param name name of the player
   * @param deck the deck of cards available to the player
   * @param handSize the size of the player's hand.
   * @throws IllegalArgumentException if handsize is greater than 1/3 deck size
   */
  public AbstractPlayer(String name, IDeck deck, int handSize) {
    this.name = name;
    this.deck = deck;
    if (handSize > (deck.size() / 3)) {
      throw new IllegalArgumentException("hand size cannot be greater than 1/3 deck size");
    }
    this.hand = new ArrayList<>(handSize);
  }

  @Override
  public IDeck getDeck() {
    return deck;
  }

  @Override
  public List<ICard> getHand() {
    return new ArrayList<>(hand);
  }

  @Override
  public void drawCard() {
    ICard drawn = deck.drawCard();
    if (drawn != null) {
      hand.add(drawn);
    }
  }

  @Override
  public void removeCard(ICard card) {
    this.hand.remove(card);
  }

  @Override
  public String getName() {
    return this.name;
  }
}
