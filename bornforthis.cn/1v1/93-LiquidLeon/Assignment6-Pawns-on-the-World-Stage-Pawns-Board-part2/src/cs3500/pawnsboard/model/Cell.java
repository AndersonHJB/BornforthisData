package cs3500.pawnsboard.model;

/**
 * Represents a single cell on the board in the game Pawns Board.
 * A cell can contain a card, a number of pawns (0 to 3), or be empty.
 * Pawns can belong to either player and may be influenced by placed cards.
 */
public class Cell implements ICell {
  private ICard card;
  private int pawns;
  private boolean ownedByRed;

  /**
   * Constructs ane mpty cell with no card nor pawns.
   */
  public Cell() {
    this.card = null;
    this.pawns = 0;
    this.ownedByRed = false;
  }

  @Override
  public boolean isEmpty() {
    return (!hasCard() && !hasPawns());
  }

  @Override
  public boolean hasCard() {
    return this.card != null;
  }

  @Override
  public boolean hasPawns() {
    return pawns > 0;
  }

  @Override
  public int getPawnCount() {
    return pawns;
  }

  @Override
  public ICard getCard() {
    return this.card;
  }

  @Override
  public void placeCard(ICard c, boolean isRed) {
    if (hasCard()) {
      throw new IllegalStateException("Cell occupied");
    }
    if (c.getCost() > pawns) {
      throw new IllegalArgumentException("The cost is more than the number of pawns");
    }
    if (this.hasPawns() && this.isOwnedByRed() != isRed) {
      throw new IllegalArgumentException("The pawns are not owned by the player");
    }
    this.card = c;
    this.pawns = 0;
    this.ownedByRed = isRed;
  }

  @Override
  public void addPawns(int count, boolean isRed) {
    if (count < 0) {
      throw new IllegalArgumentException("Count cannot be negative");
    }
    this.pawns = Math.min(this.pawns + count, 3);
    this.ownedByRed = isRed;
  }

  @Override
  public void switchPawnsOwnership() {
    this.ownedByRed = !this.ownedByRed;
  }

  @Override
  public boolean isOwnedByRed() {
    return this.ownedByRed;
  }

  @Override
  public String toString() {
    if (hasCard()) {
      return (ownedByRed ? "R" : "B") + card.toString();
    }
    else if (hasPawns()) {
      return Integer.toString(pawns);
    }
    else {
      return "_";
    }
  }
}
