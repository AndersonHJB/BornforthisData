package cs3500.pawnsboard.view;

import cs3500.pawnsboard.model.IBoard;
import cs3500.pawnsboard.model.ICell;
import cs3500.pawnsboard.model.IPawnsBoardModel;

/**
 * Implements a textual view for the Pawns Board game.
 * Displays the board with row scores, pawns, and placed cards.
 */
public class TextualPawnsBoardView implements ITextualView {

  @Override
  public StringBuilder render(IPawnsBoardModel model) {
    IBoard board = model.getBoard();
    int rows = board.getRows();
    int cols = board.getCols();
    StringBuilder app = new StringBuilder();

    for (int x = 0; x < rows; x++) {
      int redRowPoints = 0;
      int blueRowPoints = 0;
      app.append(getRowPoints(board, x, true)).append(" ");

      for (int y = 0; y < cols; y++) {
        app.append(board.getCell(x,y).toString());
      }

      app.append(" ").append(getRowPoints(board, x, false)).append("\n");
    }
    return app;
  }

  @Override
  public void printBoard(IPawnsBoardModel model) {
    System.out.println(this.render(model));
  }

  /**
   * Calculates the row score for a given player, red or blue.
   * @param board the game board
   * @param x the row index
   * @param isRed whether to calcualte to red or blue player
   * @return the total score for that player in the given row
   */
  private int getRowPoints(IBoard board, int x, boolean isRed) {
    int score = 0;
    for (int y = 0; y < board.getCols(); y++) {
      ICell cell = board.getCell(x,y);
      if (cell.hasCard()) {
        if (cell.isOwnedByRed() == isRed) {
          score += cell.getCard().getValue();
        }
      }
    }
    return score;
  }
}

