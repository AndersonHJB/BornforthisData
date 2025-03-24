package cs3500.pawnsboard.model;

/**
 * Represents the different possible states of a Pawns Board game.
 * THis determines whether the game is ongoing, completed with a winner,
 * or has ended in a tie.
 */
public enum GameState {
  NOT_STARTED,
  ONGOING,
  RED_WINS,
  BLUE_WINS,
  TIE
}
