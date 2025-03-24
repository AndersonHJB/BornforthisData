package cs3500.pawnsboard.model;

import java.util.Objects;

/**
 * An abstract class that provides base functionalities for different card types in
 * the future.
 */
public class AbstractCard implements ICard {
  protected final String name;
  protected final int cost;
  protected final int value;
  protected final IInfluenceGrid influence;

  /**
   * Constrcuts a Card with the given arguments.
   * INVARIANT: cost is between 1 and 3 inclusive.
   * INVARIANT: value is positive.
   * @param name the name of the card
   * @param cost the cost in pawns required to play
   * @param value the point value of the card
   * @param influence the 5x5 influence grid
   * @throws IllegalArgumentException if cost is not between 1 and 3 or value isn't positive.
   */
  public AbstractCard(String name, int cost, int value, IInfluenceGrid influence) {
    if (cost < 1 || cost > 3) {
      throw new IllegalArgumentException("cost must be between 1 and 3");
    }
    if (value <= 0) {
      throw new IllegalArgumentException("value must be positive");
    }
    this.name = name;
    this.cost = cost;
    this.value = value;
    this.influence = influence;
  }

  @Override
  public String getName() {
    return this.name;
  }

  @Override
  public int getCost() {
    return this.cost;
  }

  @Override
  public int getValue() {
    return this.value;
  }

  @Override
  public IInfluenceGrid getInfluenceGrid() {
    return this.influence;
  }

  @Override
  public boolean equals(Object that) {
    if (!(that instanceof ICard)) {
      return false;
    }
    ICard other = (ICard) that;
    return this.getCost() == other.getCost()
            && this.getValue() == other.getValue()
            && this.getInfluenceGrid().equals(other.getInfluenceGrid())
            && this.getName().equals(other.getName());
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, cost, value, influence);
  }
}
