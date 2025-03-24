package cs3500.pawnsboard.model;

import java.util.Arrays;
import java.util.Objects;

/**
 * Represents a 5x5 influence grid for a card.
 */
public class InfluenceGrid implements IInfluenceGrid {
  private final char[][] grid;

  /**
   * Constructs an InfluenceGrid.
   * INVARIANT: the grid must be a 5x5 matrix.
   * @param grid The 5x5 influence grid.
   * @throws IllegalArgumentException if the grid isn't 5x5
   */
  public InfluenceGrid(String[] grid) {
    if (grid.length != 5) {
      throw new IllegalArgumentException("grid must be 5x5.");
    }
    for (int i = 0; i < grid.length; i++) {
      if (grid[i].length() != 5) {
        throw new IllegalArgumentException("grid must be 5x5.");
      }
    }
    this.grid = new char[5][5];
    for (int i = 0; i < grid.length; i++) {
      this.grid[i] = grid[i].toCharArray();
    }
  }

  @Override
  public boolean isInfluenced(int x, int y) {
    return (x >= 0 && x < 5 && y >= 0 && y < 5 && grid[x][y] == 'I');
  }

  @Override
  public char[][] getGrid() {
    return grid;
  }

  @Override
  public boolean equals(Object that) {
    if (!(that instanceof IInfluenceGrid)) {
      return false;
    }
    IInfluenceGrid other = (IInfluenceGrid) that;
    return Arrays.deepEquals(this.getGrid(), other.getGrid());
  }

  @Override
  public int hashCode() {
    return Objects.hash(grid);
  }
}
