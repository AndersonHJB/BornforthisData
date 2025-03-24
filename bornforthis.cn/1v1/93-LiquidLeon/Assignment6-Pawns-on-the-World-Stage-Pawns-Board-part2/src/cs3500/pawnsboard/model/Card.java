package cs3500.pawnsboard.model;

/**
 * Represents a card in the Pawns Board.
 * Each card has a name, a cost in pawns, a value score, and a 5x5 influence grid
 * that defines how it affects the board.
 */
public class Card extends AbstractCard {

  /**
   * Constrcuts a Card with the given arguments.
   * @param name the name of the card
   * @param cost the cost in pawns required to play
   * @param value the point value of the card
   * @param influence the 5x5 influence grid
   * @throws IllegalArgumentException if cost is not between 1 and 3 or value isn't positive.
   */
  public Card(String name, int cost, int value, IInfluenceGrid influence) {
    super(name,cost,value,influence);
  }

  @Override
  public String toString() {
    return "";
  }
}