package cs3500.pawnsboard.model;

/**
 * Represents a card's influence grid.
 */
public interface IInfluenceGrid {
  /**
   * Checks if a cell is influenced.
   * @param x the row index
   * @param y the column index
   * @return true if the cell is influenced, false otherwise.
   */
  boolean isInfluenced(int x, int y);

  /**
   * Returns the influence grid.
   * @return the influence grid.
   */
  char[][] getGrid();

  /**
   * Checks if this grid is the same as the given grid.
   * @param other the given grid.
   * @return true if they are the same, false otherwise.
   */
  boolean equals(Object other);
}
