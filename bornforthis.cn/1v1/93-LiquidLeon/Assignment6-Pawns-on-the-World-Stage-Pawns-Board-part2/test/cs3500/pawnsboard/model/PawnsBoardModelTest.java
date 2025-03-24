package cs3500.pawnsboard.model;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;

/**
 * A test class for the model portion of the Pawns Board game.
 * Tests PawnsBoardModelImpl, Card, Board,
 * Deck, Cell and Player class
 */
public class PawnsBoardModelTest {
  private PawnsBoardModelImpl model;
  private IBoard board;
  private IPlayer redPlayer;
  private IPlayer bluePlayer;
  private List<ICard>[] decks;
  private ICard card1;
  private ICard card2;

  @Before
  public void setUp() {
    try {
      String filePath = "Assignment05" + File.separator +
              "docs" + File.separator + "deck.config";
      decks = DeckReader.readDeckFile(filePath);
    } catch (FileNotFoundException e) {
      Assert.fail("Deck file not found.");
    }

    IDeck redDeck = new Deck(decks[0]);
    IDeck blueDeck = new Deck(decks[1]);
    redPlayer = new Player("Red", redDeck, 5);
    bluePlayer = new Player("Blue", blueDeck, 5);

    board = new Board(3, 5);

    model = new PawnsBoardModelImpl(board, redPlayer, bluePlayer, 5);

    card1 = new Card(
            "Guardian",
            1,
            3,
            new InfluenceGrid(new String[]{
                "XXXXX",
                "XXIXX",
                "XICIX",
                "XXIXX",
                "XXXXX"}
            ));

    card2 = new Card(
            "Bee",
            1,
            2,
            new InfluenceGrid(new String[]{
                "XXIXX",
                "XXXXX",
                "XXCXX",
                "XXXXX",
                "XXIXX"}
            ));
  }

  // TESTS FOR PawnsBoardModelImpl

  @Test(expected = IllegalStateException.class)
  public void testStartAlreadyStartedGame() {
    model.startGame();
    model.startGame();
  }

  @Test
  public void testStartGame() {
    model.startGame();

    Assert.assertEquals(GameState.ONGOING, model.getGameState());

    Assert.assertEquals(5, redPlayer.getHand().size());
    Assert.assertEquals(5, bluePlayer.getHand().size());

    for (int row = 0; row < board.getRows(); row++) {
      Assert.assertEquals(1, board.getCell(row, 0).getPawnCount());
      Assert.assertEquals(true, board.getCell(row, 0).isOwnedByRed());

      Assert.assertEquals(1, board.getCell(row, board.getCols() - 1).getPawnCount());
      Assert.assertEquals(false, board.getCell(row, board.getCols() - 1).isOwnedByRed());
    }
  }

  @Test(expected = IllegalStateException.class)
  public void testPlaceCardBeforeGameStarts() {
    model.placeCard(0, 0, decks[0].get(0));
  }

  @Test(expected = IllegalStateException.class)
  public void testPLaceCardAfterGameEnds() {
    model.startGame();
    model.passTurn();
    model.passTurn();
    model.placeCard(0, 0, redPlayer.getHand().get(0));
  }

  @Test(expected = IllegalArgumentException.class)
  public void testPlaceCardWithoutEnoughPawns() {
    model.startGame();
    model.placeCard(1, 1, card1);
  }

  @Test
  public void testConvertPawns() {
    model.startGame();
    ICard testCard = new Card("Converter", 1, 3, new InfluenceGrid(new String[]{
        "XXXXX",
        "XXXXX",
        "IXCXI",
        "XXXXX",
        "XXXXX"
    }));
    board.placeCard(0, 0, testCard, true);
    board.placeCard(0, 4, testCard, false);

    Assert.assertFalse(board.getCell(1, 2).isOwnedByRed());
  }

  @Test
  public void testTIE() {
    model.startGame();

    ICard redCard = redPlayer.getHand().get(0);
    ICard blueCard = bluePlayer.getHand().get(0);

    model.placeCard(0, 0, redCard);
    model.placeCard(2, 4, blueCard);

    model.passTurn();
    model.passTurn();

    Assert.assertEquals(GameState.TIE, model.getGameState());
  }

  @Test
  public void testRedWin() {
    model.startGame();

    ICard redCard = redPlayer.getHand().get(0);
    ICard blueCard = bluePlayer.getHand().get(1);

    model.placeCard(0, 0, redCard);
    model.placeCard(2, 4, blueCard);

    model.passTurn();
    model.passTurn();

    Assert.assertEquals(GameState.RED_WINS, model.getGameState());
  }

  @Test
  public void tesBlueWin() {
    model.startGame();

    ICard redCard = redPlayer.getHand().get(1);
    ICard blueCard = bluePlayer.getHand().get(0);

    model.placeCard(0, 0, redCard);
    model.placeCard(2, 4, blueCard);

    model.passTurn();
    model.passTurn();

    Assert.assertEquals(GameState.BLUE_WINS, model.getGameState());
  }


  @Test
  public void testApplyInfluence() {
    model.startGame();
    ICard card = redPlayer.getHand().get(0);
    model.placeCard(1, 0, card);

    Assert.assertEquals(true, board.getCell(0, 0).hasPawns());
    Assert.assertEquals(true, board.getCell(2, 0).hasPawns());
    Assert.assertEquals(true, board.getCell(1, 1).hasPawns());

    model.placeCard(0, 4, card);

    Assert.assertEquals(true, board.getCell(1, 4).hasPawns());
    Assert.assertEquals(true, board.getCell(0, 4).hasCard());
  }

  @Test
  public void testOutOfBound() {
    Assert.assertTrue(model.outOfBound(-1, 0));
    Assert.assertTrue(model.outOfBound(5, 2));
    Assert.assertTrue(model.outOfBound(0, -1));
    Assert.assertTrue(model.outOfBound(0, 5));
    Assert.assertFalse(model.outOfBound(2, 2));
  }

  @Test
  public void testIsPlayerDone() {
    model.startGame();
    Assert.assertTrue(model.isPlayerDone(redPlayer));
    Assert.assertTrue(model.isPlayerDone(bluePlayer));

    model.placeCard(1, 0, redPlayer.getHand().get(0));
    model.placeCard(2, 4, bluePlayer.getHand().get(1));
    model.passTurn();
    model.placeCard(0, 4, bluePlayer.getHand().get(0));
    model.placeCard(0, 0, redPlayer.getHand().get(0));
    model.placeCard(1, 4, bluePlayer.getHand().get(0));
    model.placeCard(2, 0, redPlayer.getHand().get(0));
    model.placeCard(0, 3, bluePlayer.getHand().get(2));
    model.placeCard(1, 1, redPlayer.getHand().get(2));
    model.placeCard(1, 3, bluePlayer.getHand().get(4));
    model.placeCard(2, 1, redPlayer.getHand().get(2));
    model.passTurn();
    model.placeCard(0, 1, redPlayer.getHand().get(3));

    Assert.assertFalse(model.isPlayerDone(redPlayer));
    Assert.assertFalse(model.isPlayerDone(bluePlayer));
  }

  @Test(expected = IllegalStateException.class)
  public void testPassTurnBeforeGame() {
    model.passTurn();
  }

  @Test
  public void testPassTurnAndGetGameState() {
    model.startGame();
    Assert.assertEquals(GameState.ONGOING, model.getGameState());
    model.passTurn();
    Assert.assertEquals(GameState.ONGOING, model.getGameState());
    model.passTurn();
    Assert.assertNotEquals(GameState.ONGOING, model.getGameState());
    Assert.assertEquals(GameState.TIE, model.getGameState());
  }

  @Test
  public void testGetBoard() {
    Assert.assertEquals(3, model.getBoard().getRows());
    Assert.assertEquals(5, model.getBoard().getCols());
  }


  // TESTS FOR Card

  @Test
  public void testGetCost() {
    model.startGame();
    ICard card = redPlayer.getHand().get(0);
    Assert.assertEquals(1, card.getCost());
  }

  @Test
  public void testGetValue() {
    model.startGame();
    ICard card = redPlayer.getHand().get(0);
    Assert.assertEquals(3, card.getValue());
  }

  @Test
  public void testGetInfluenceGrid() {
    model.startGame();
    IInfluenceGrid grid = redPlayer.getHand().get(0).getInfluenceGrid();
    char[][] g = grid.getGrid();

    Assert.assertEquals("XXXXX", String.valueOf(g[0]));
    Assert.assertEquals("XXIXX", String.valueOf(g[1]));
    Assert.assertEquals("XICIX", String.valueOf(g[2]));
    Assert.assertEquals("XXIXX", String.valueOf(g[3]));
    Assert.assertEquals("XXXXX", String.valueOf(g[4]));
  }

  @Test
  public void testDetermineWinner() {
    model.startGame();

    model.placeCard(0, 0, redPlayer.getHand().get(0));
    model.placeCard(2, 4, bluePlayer.getHand().get(1));

    model.passTurn();
    model.passTurn();
    Assert.assertEquals(GameState.RED_WINS, model.getGameState());
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidCardCostTooLow() {
    new Card("Low", 0, 3, new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XICIX",
        "XXIXX",
        "XXXXX"}));
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidCardCostTooHigh() {
    new Card("High", 4, 3, new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XICIX",
        "XXIXX",
        "XXXXX"}));
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidCardValueZero() {
    new Card("Zero", 1, 0, new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XICIX",
        "XXIXX",
        "XXXXX"}));
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidCardValueNegative() {
    new Card("Negative", 2, -5, new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XICIX",
        "XXIXX",
        "XXXXX"}));
  }

  // TEST FOR Deck

  @Test
  public void testGetSize() {
    Assert.assertEquals(15, redPlayer.getDeck().size());
    Assert.assertEquals(15, bluePlayer.getDeck().size());
  }

  @Test
  public void testDrawCard() {
    Assert.assertEquals(0, redPlayer.getHand().size());
    redPlayer.drawCard();
    Assert.assertEquals(1, redPlayer.getHand().size());
  }

  @Test
  public void testEmptyDeck() {
    IDeck emptyDeck = new Deck(new ArrayList<>());
    Assert.assertEquals(0, emptyDeck.size());
    Assert.assertNull(emptyDeck.drawCard());
  }

  @Test
  public void testDrawAllCards() {
    List<ICard> cards = new ArrayList<>();
    cards.add(card1);
    cards.add(card2);
    IDeck deck = new Deck(cards);

    Assert.assertEquals(2, deck.size());

    ICard drawn1 = deck.drawCard();
    Assert.assertEquals(card1, drawn1);
    Assert.assertEquals(1, deck.size());

    ICard drawn2 = deck.drawCard();
    Assert.assertEquals(card2, drawn2);
    Assert.assertEquals(0, deck.size());

    Assert.assertNull(deck.drawCard());
  }


  // TEST FOR Cell

  @Test
  public void testIsEmpty() {
    Assert.assertTrue(board.getCell(0, 0).isEmpty());
    model.startGame();
    model.placeCard(0, 0, redPlayer.getHand().get(0));
    Assert.assertFalse(board.getCell(0, 0).isEmpty());
  }

  @Test
  public void testHasCard() {
    model.startGame();
    Assert.assertFalse(board.getCell(0, 0).hasCard());
    model.placeCard(0, 0, redPlayer.getHand().get(0));
    Assert.assertTrue(board.getCell(0, 0).hasCard());
  }

  @Test
  public void testHasPawns() {
    model.startGame();
    Assert.assertFalse(board.getCell(0, 1).hasPawns());
    Assert.assertTrue(board.getCell(0, 0).hasPawns());
  }

  @Test
  public void testGetPawnCount() {
    model.startGame();
    Assert.assertEquals(1, board.getCell(0, 0).getPawnCount());
    model.placeCard(1, 0, redPlayer.getHand().get(0));
    Assert.assertEquals(2, board.getCell(0, 0).getPawnCount());
  }

  @Test
  public void testPlaceCardInCell() {
    model.startGame();
    ICell testCell = board.getCell(0, 0);
    Assert.assertEquals(1, testCell.getPawnCount());
    testCell.placeCard(redPlayer.getHand().get(0), true);
    Assert.assertEquals(0, testCell.getPawnCount());
    Assert.assertTrue(board.getCell(0, 0).hasCard());

    Assert.assertThrows(IllegalStateException.class, () -> {
      testCell.placeCard(redPlayer.getHand().get(0), true);
    });

    ICell invalidCell = board.getCell(1, 2);

    Assert.assertThrows(IllegalArgumentException.class, () -> {
      invalidCell.placeCard(redPlayer.getHand().get(0), false);
    });
  }

  @Test(expected = IllegalArgumentException.class)
  public void testPlaceCardNotEnoughPawns() {
    ICell cell = new Cell();
    ICard expensiveCard = new Card("Expensive", 3, 5, new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XICIX",
        "XXIXX",
        "XXXXX"
    }));

    cell.addPawns(1, true);
    cell.placeCard(expensiveCard, true);
  }


  @Test
  public void testAddPawns() {
    model.startGame();
    ICell testCell = board.getCell(0, 0);
    Assert.assertThrows(IllegalArgumentException.class, () -> {
      testCell.addPawns(-1, true);
    });

    testCell.addPawns(2, true);
    Assert.assertEquals(3, testCell.getPawnCount());

    testCell.addPawns(1, true);
    Assert.assertEquals(3, testCell.getPawnCount());
  }

  @Test
  public void testSwitchPawnsOwnershipAndIsOwnedByRed() {
    model.startGame();
    ICell testCell = board.getCell(0, 0);
    Assert.assertTrue(testCell.isOwnedByRed());

    testCell.switchPawnsOwnership();
    Assert.assertFalse(testCell.isOwnedByRed());
  }

  @Test
  public void testToStringForCell() {
    model.startGame();
    Assert.assertEquals("1", board.getCell(0, 0).toString());
    Assert.assertEquals("_", board.getCell(0, 1).toString());

    model.placeCard(0, 0, redPlayer.getHand().get(0));
    Assert.assertEquals("R", board.getCell(0, 0).toString());

    model.placeCard(0, 4, redPlayer.getHand().get(0));
    Assert.assertEquals("B", board.getCell(0, 4).toString());
  }

  @Test
  public void testNewEmptyCell() {
    ICell cell = new Cell();
    Assert.assertTrue(cell.isEmpty());
    Assert.assertFalse(cell.hasCard());
    Assert.assertFalse(cell.hasPawns());
    Assert.assertEquals(0, cell.getPawnCount());
  }

  @Test(expected = IllegalArgumentException.class)
  public void testPlaceCardOnOpponentPawns() {
    model.startGame();
    ICell cell = board.getCell(1, 2);
    cell.addPawns(1, false);
    cell.placeCard(card1, true);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testOpponentPlacingCardAfterOwnershipSwitch() {
    model.startGame();
    ICell cell = board.getCell(1, 2);

    cell.addPawns(2, true);
    cell.switchPawnsOwnership();
    cell.placeCard(card2, true);
  }


  // TEST FOR Board

  @Test
  public void testGetRowsGetCols() {
    model.startGame();
    Assert.assertEquals(3, model.getBoard().getRows());
    Assert.assertEquals(5, model.getBoard().getCols());
  }

  @Test
  public void testPlaceCardInBoard() {
    model.startGame();
    Assert.assertFalse(board.getCell(0, 0).hasCard());
    board.placeCard(0, 0, redPlayer.getHand().get(0), true);
    Assert.assertTrue(board.getCell(0, 0).hasCard());
  }

  @Test
  public void testValidBoardCreation() {
    IBoard board = new Board(3, 5);
    Assert.assertEquals(3, board.getRows());
    Assert.assertEquals(5, board.getCols());
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidBoardCreationNegativeRows() {
    new Board(-1, 5);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidBoardCreationZeroRows() {
    new Board(0, 5);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidBoardCreationOneColumn() {
    new Board(3, 1);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidBoardCreationEvenColumns() {
    new Board(3, 4);
  }

  @Test
  public void testGetCellValidCoordinates() {
    Assert.assertNotNull(board.getCell(0, 0));
    Assert.assertNotNull(board.getCell(2, 4));
  }

  @Test(expected = ArrayIndexOutOfBoundsException.class)
  public void testGetCellNegativeCoordinates() {
    board.getCell(-1, 0);
  }

  @Test(expected = ArrayIndexOutOfBoundsException.class)
  public void testGetCellOutOfBoundsRow() {
    board.getCell(3, 2);
  }

  @Test(expected = ArrayIndexOutOfBoundsException.class)
  public void testGetCellOutOfBoundsColumn() {
    board.getCell(1, 5);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testPlaceCardWithoutEnoughPawnsInBoard() {
    board.placeCard(1, 1, card1, true);
  }

  @Test(expected = IllegalStateException.class)
  public void testPlaceCardOnOccupiedCell() {
    board.getCell(1, 1).addPawns(1, true);
    board.placeCard(1, 1, card1, true);
    board.placeCard(1, 1, card2, false);
  }


  // TEST FOR Player

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidPlayerInitialization() {
    IDeck testDeck = new Deck(new ArrayList<>());
    IPlayer player = new Player("test", testDeck, 5);

    Assert.assertEquals(testDeck, player.getDeck());
    Assert.assertTrue(player.getHand().isEmpty());
  }

  @Test
  public void testGetDeck() {
    IDeck deck = redPlayer.getDeck();
    Assert.assertEquals(15, deck.size());

    Assert.assertTrue(card1.equals(deck.drawCard()));
  }


  @Test
  public void testGetHand() {
    Assert.assertTrue(redPlayer.getHand().isEmpty());
    model.startGame();
    List<ICard> hand = redPlayer.getHand();

    Assert.assertEquals(5, hand.size());
    Assert.assertTrue(card1.equals(hand.get(0)));
    Assert.assertTrue(card2.equals(hand.get(1)));
  }

  @Test
  public void testDrawCardInPlayer() {
    redPlayer.drawCard();
    Assert.assertEquals(1, redPlayer.getHand().size());
    Assert.assertTrue(card1.equals(redPlayer.getHand().get(0)));
  }

  @Test
  public void testRemoveCard() {
    redPlayer.drawCard();
    Assert.assertEquals(1, redPlayer.getHand().size());

    redPlayer.removeCard(card2);
    Assert.assertEquals(1, redPlayer.getHand().size());

    redPlayer.removeCard(card1);
    Assert.assertEquals(0, redPlayer.getHand().size());
  }


  // TEST FOR InfluenceGrid

  @Test
  public void testInfluenceGrid() {
    IInfluenceGrid grid = new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XICIX",
        "XXIXX",
        "XXXXX"
    });

    char[][] expected = {
            {'X', 'X', 'X', 'X', 'X'},
            {'X', 'X', 'I', 'X', 'X'},
            {'X', 'I', 'C', 'I', 'X'},
            {'X', 'X', 'I', 'X', 'X'},
            {'X', 'X', 'X', 'X', 'X'}
    };

    Assert.assertArrayEquals(expected, grid.getGrid());
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidInfluenceGridTooSmall() {
    new InfluenceGrid(new String[]{
        "XXXX",
        "XXIX",
        "XICI",
        "XXIX"
    });
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidInfluenceGridTooLarge() {
    new InfluenceGrid(new String[]{
        "XXXXXX",
        "XXIXXX",
        "XICICX",
        "XXIXXX",
        "XXXXXX",
        "XXXXXX"
    });
  }

  @Test(expected = IllegalArgumentException.class)
  public void testInvalidInfluenceGridWrongRowSizes() {
    new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XIC",
        "XXIXX",
        "XXXXX"
    });
  }


  @Test
  public void testIsInfluenced() {
    IInfluenceGrid grid = new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XICIX",
        "XXIXX",
        "XXXXX"
    });

    Assert.assertTrue(grid.isInfluenced(1, 2));
    Assert.assertTrue(grid.isInfluenced(2, 1));
    Assert.assertTrue(grid.isInfluenced(2, 3));

    Assert.assertFalse(grid.isInfluenced(0, 0));
    Assert.assertFalse(grid.isInfluenced(4, 4));
    Assert.assertFalse(grid.isInfluenced(2, 2));

    Assert.assertFalse(grid.isInfluenced(-1, 0));
    Assert.assertFalse(grid.isInfluenced(5, 0));
    Assert.assertFalse(grid.isInfluenced(0, -1));
    Assert.assertFalse(grid.isInfluenced(0, 5));
  }

  @Test
  public void testBlueDeckHasReversedInfluenceGrid() {
    for (int i = 0; i < decks[0].size(); i++) {
      ICard redCard = decks[0].get(i);
      ICard blueCard = decks[1].get(i);

      Assert.assertEquals(redCard.getName(), blueCard.getName());
      Assert.assertEquals(redCard.getCost(), blueCard.getCost());
      Assert.assertEquals(redCard.getValue(), blueCard.getValue());

      char[][] redGrid = redCard.getInfluenceGrid().getGrid();
      char[][] blueGrid = blueCard.getInfluenceGrid().getGrid();

      for (int row = 0; row < 5; row++) {
        String red = new String(redGrid[row]);
        String blue = new String(blueGrid[row]);
        String reversed = new StringBuilder(red).reverse().toString();

        Assert.assertEquals(reversed, blue);
      }


    }
  }
}
