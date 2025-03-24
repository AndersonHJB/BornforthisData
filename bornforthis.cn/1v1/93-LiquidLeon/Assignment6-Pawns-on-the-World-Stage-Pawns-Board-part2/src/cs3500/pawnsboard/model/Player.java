package cs3500.pawnsboard.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Represents a player in the Pawns Board game.
 */
public class Player extends AbstractPlayer {
  List<ICard> hand;

  public Player(String name, IDeck deck, int handSize) {
    super(name, deck, handSize);
    this.hand = new ArrayList<>(handSize);
  }
}
