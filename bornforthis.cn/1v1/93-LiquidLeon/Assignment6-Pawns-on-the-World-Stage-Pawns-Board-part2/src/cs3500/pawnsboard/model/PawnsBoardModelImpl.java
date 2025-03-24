package cs3500.pawnsboard.model;

/**
 * Implements the game logic for Pawns Board.
 * This class handles the player turns, move legality and applies card influences.
 */
public class PawnsBoardModelImpl implements IPawnsBoardModel {
  private final IBoard board;
  private final IPlayer red;
  private final IPlayer blue;
  private boolean isRed;
  private boolean redPassed;
  private boolean bluePassed;
  private GameState gameState;
  private final int handSize;

  /**
   * Constructs a new Pawns Board game model with the specified board and players.
   * The game starts with red player.
   * @param board the board on which the game is played on
   * @param red red player
   * @param blue blue player
   * @param handSize number of cards in the player's hand
   */
  public PawnsBoardModelImpl(IBoard board, IPlayer red, IPlayer blue, int handSize) {
    this.board = board;
    this.red = red;
    this.blue = blue;
    this.isRed = true;
    this.redPassed = false;
    this.bluePassed = false;
    this.handSize = handSize;
    this.gameState = GameState.NOT_STARTED;
  }

  @Override
  public void startGame() {
    if (gameState != GameState.NOT_STARTED) {
      throw new IllegalStateException("Game has already started");
    }
    for (int i = 0; i < handSize; i++) {
      red.drawCard();
      blue.drawCard();
    }
    for (int x = 0; x < board.getRows(); x++) {
      board.getCell(x, 0).addPawns(1, true);
      board.getCell(x, board.getCols() - 1).addPawns(1, false);
    }
    gameState = GameState.ONGOING;
  }

  @Override
  public void placeCard(int x, int y, ICard card) {
    if (gameState == GameState.NOT_STARTED) {
      throw new IllegalStateException("Game hasn't started");
    }
    if (gameState != GameState.ONGOING) {
      throw new IllegalStateException("Game has ended");
    }

    IPlayer current = isRed ? red : blue;
    if (!current.getHand().contains(card)) {
      throw new IllegalArgumentException("Current player doesn't have the card");
    }

    try {
      board.placeCard(x,y,card,isRed);
      applyInfluence(x,y,card);
      current.removeCard(card);
      current.drawCard();
    } catch (Exception e) {
      System.out.println("Invalid Move: " + e.getMessage());
      throw e;
    }

    if (isRed) {
      redPassed = false;
    }
    else {
      bluePassed = false;
    }
    isRed = !isRed;
    checkGameOver();
  }

  /**
   * Applies the influence pattern of the placed card to the board.
   * @param x the row index
   * @param y the column index
   * @param card the card being placed
   */
  private void applyInfluence(int x, int y, ICard card) {
    IInfluenceGrid grid = card.getInfluenceGrid();
    for (int i = -2; i <= 2; i++) {
      for (int j = -2; j <= 2; j++) {
        int targetX = x + i;
        int targetY = y + j;
        if (outOfBound(targetX,targetY)) {
          continue;
        }

        boolean isEffected = grid.isInfluenced(i + 2, j + 2);
        if (isEffected) {
          ICell targetCell = board.getCell(targetX, targetY);
          if (!targetCell.hasCard()) {
            if (!targetCell.hasPawns()) {
              targetCell.addPawns(1, isRed);
            }
            else {
              if ((isRed && !targetCell.isOwnedByRed()) ||
                      (!isRed && targetCell.isOwnedByRed())) {
                targetCell.switchPawnsOwnership();
              }
              else {
                targetCell.addPawns(1, isRed);
              }
            }
          }
        }
      }
    }
  }

  /**
   * Checks if the given coordinate is out of bounds of the game baord.
   * @param x the row index
   * @param y the column index
   * @return true if the coordinate is out of bounds, false otherwise
   */
  boolean outOfBound(int x, int y) {
    return x < 0 || x > board.getRows() - 1 || y < 0 || y > board.getCols() - 1;
  }

  /**
   * Checks if the game is over based on whether either players can make more valid moves.
   */
  private void checkGameOver() {
    boolean isRedDone = isPlayerDone(red);
    boolean isBlueDone = isPlayerDone(blue);

    if (isRedDone && isBlueDone) {
      determineWinner();
    }
  }

  /**
   * Determines if a given player has any valid moves left.
   * @param player the given player
   * @return false if the player can't move anymore, true otherwise
   */
  boolean isPlayerDone(IPlayer player) {
    for (ICard card : player.getHand()) {
      for (int row = 0; row < board.getRows(); row++) {
        for (int col = 0; col < board.getCols(); col++) {
          ICell cell = board.getCell(row, col);
          if (!cell.hasCard() && cell.hasPawns() && card.getCost() <= cell.getPawnCount()) {
            return false;
          }
        }
      }
    }
    return true;
  }

  @Override
  public void passTurn() {
    if (gameState == GameState.NOT_STARTED) {
      throw new IllegalStateException("Game hasn't started");
    }
    if (gameState != GameState.ONGOING) {
      throw new IllegalStateException("Game has ended");
    }

    if (isRed) {
      redPassed = true;
    }
    else {
      bluePassed = true;
    }

    if (redPassed && bluePassed) {
      determineWinner();
    }
    isRed = !isRed;
  }

  /**
   * Determines the winner of the game by calculating scores for each row.
   * Player with the higher score wins.
   */
  private void determineWinner() {
    int redScore = 0;
    int blueScore = 0;

    for (int row = 0; row < board.getRows(); row++) {
      int redRow = 0;
      int blueRow = 0;
      for (int col = 0; col < board.getCols(); col++) {
        ICell cell = board.getCell(row, col);
        if (cell.hasCard()) {
          ICard card = cell.getCard();
          if (cell.isOwnedByRed()) {
            redRow += card.getValue();
          } else {
            blueRow += card.getValue();
          }
        }
      }
      if (redRow > blueRow) {
        redScore += redRow;
      } else if (blueRow > redRow) {
        blueScore += blueRow;
      }
    }
    if (redScore > blueScore) {
      gameState = GameState.RED_WINS;
    } else if (blueScore > redScore) {
      gameState = GameState.BLUE_WINS;
    } else {
      gameState = GameState.TIE;
    }
  }

  @Override
  public GameState getGameState() {
    return gameState;
  }

  @Override
  public IBoard getBoard() {
    return board;
  }
  @Override
  public IPlayer getCurrentPlayer() {
    return isRed ? red : blue;
  }

  @Override
  public boolean isLegalMove(int x, int y, ICard card) {
    if (gameState != GameState.ONGOING) return false;
    ICell cell = board.getCell(x, y);
    if (cell.hasCard()) return false;
    boolean currentIsRed = isRed;
    if (cell.hasPawns()) {
      if (card.getCost() > cell.getPawnCount()) return false;
      if (cell.isOwnedByRed() != currentIsRed) return false;
    } else {
      return false;
    }
    return true;
  }
}
