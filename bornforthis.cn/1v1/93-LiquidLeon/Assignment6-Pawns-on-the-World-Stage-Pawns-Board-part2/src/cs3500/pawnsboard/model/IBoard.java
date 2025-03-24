package cs3500.pawnsboard.model;

/**
 * Represents the board in Pawns Board.
 */
public interface IBoard {
  /**
   * Returns the number of rows of the board.
   * @return the number of rows
   */
  int getRows();

  /**
   * Returns the number of columns of the board.
   * @return the number of columns
   */
  int getCols();

  /**
   * Returns the cell at the given corrdinate.
   * @param x the row index
   * @param y the column index
   * @return the cell at the given indices.
   */
  ICell getCell(int x, int y);

  /**
   * Places a card at the given coordinate.
   * @param x the row index
   * @param y the column index
   * @param card the card to be placed at the cell
   * @param isRed true if the red player placed it, false otherwise
   */
  void placeCard(int x, int y, ICard card, boolean isRed);

}
