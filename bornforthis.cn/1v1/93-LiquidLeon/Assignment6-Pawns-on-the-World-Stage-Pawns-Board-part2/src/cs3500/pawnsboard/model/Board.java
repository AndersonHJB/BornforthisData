package cs3500.pawnsboard.model;

/**
 * Represents the board as a rectangular grid of cells.
 */
public class Board implements IBoard {
  private final int rows;
  private final int cols;
  private final ICell[][] grid;

  /**
   * Constructs a game board with the given width and height.
   * INVARIANT: The number of columns is odd and greater than 1.
   * INVARIANT: the number of rows is greater than 0;
   * @param rows number of rows.
   * @param cols number of columns
   */
  public Board(int rows, int cols) {
    if (rows <= 0 || cols <= 1 || cols % 2 == 0) {
      throw new IllegalArgumentException("Invalid board dimensions");
    }
    this.rows = rows;
    this.cols = cols;
    this.grid = new ICell[rows][cols];
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        grid[r][c] = new Cell();
      }
    }
  }

  @Override
  public int getRows() {
    return rows;
  }

  @Override
  public int getCols() {
    return cols;
  }

  @Override
  public ICell getCell(int x, int y) {
    return grid[x][y];
  }

  @Override
  public void placeCard(int x, int y, ICard card, boolean isRed) {
    getCell(x,y).placeCard(card,isRed);
  }
}
