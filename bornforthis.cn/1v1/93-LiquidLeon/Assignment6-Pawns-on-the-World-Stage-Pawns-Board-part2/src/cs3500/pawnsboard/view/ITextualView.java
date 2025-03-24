package cs3500.pawnsboard.view;

import cs3500.pawnsboard.model.IPawnsBoardModel;

/**
 * Represents a textaul view of the Pawns Board game.
 * Provides method to render the current state of the game.
 */
public interface ITextualView {
  /**
   * Renders the current state of the board as a text representation.
   * @param model The game model to visualize
   */
  StringBuilder render(IPawnsBoardModel model);

  /**
   * Prints the textual representation of the game board to the console.
   * @param model the game model
   */
  void printBoard(IPawnsBoardModel model);
}
