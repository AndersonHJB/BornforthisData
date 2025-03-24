package cs3500.pawnsboard.view;


import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.List;
import java.util.ArrayList;

import cs3500.pawnsboard.model.Board;
import cs3500.pawnsboard.model.Card;
import cs3500.pawnsboard.model.Deck;
import cs3500.pawnsboard.model.IBoard;
import cs3500.pawnsboard.model.ICard;
import cs3500.pawnsboard.model.IDeck;
import cs3500.pawnsboard.model.IPlayer;
import cs3500.pawnsboard.model.InfluenceGrid;
import cs3500.pawnsboard.model.PawnsBoardModelImpl;
import cs3500.pawnsboard.model.Player;

/**
 * Test class the for textual view of the game baord.
 */
public class PawnsBoardViewTest {
  private TextualPawnsBoardView view;
  private PawnsBoardModelImpl model;
  private ICard card1;
  private ICard card2;
  private Appendable output;

  @Before
  public void setUp() {
    output = new StringBuilder();

    List<ICard> deck = new ArrayList<>();
    card1 = new Card("Guardian", 1, 3, new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XICIX",
        "XXIXX",
        "XXXXX"}));
    card2 = new Card("Bee", 1, 2, new InfluenceGrid(new String[]{
        "XXIXX",
        "XXXXX",
        "XXCXX",
        "XXXXX",
        "XXIXX"}));
    ICard card3 = new Card("Cee", 1, 1, new InfluenceGrid(new String[]{
        "XXXXX",
        "XXIXX",
        "XXCXX",
        "XXIXX",
        "XXXXX"}));

    deck.add(card1);
    deck.add(card2);
    deck.add(card3);

    IDeck redDeck = new Deck(deck);
    IDeck blueDeck = new Deck(deck);

    IPlayer redPlayer = new Player("Red", redDeck, 1);
    IPlayer bluePlayer = new Player("Blue", blueDeck, 1);

    IBoard board = new Board(3, 5);
    model = new PawnsBoardModelImpl(board, redPlayer, bluePlayer, 5);
    view = new TextualPawnsBoardView();
  }

  @Test
  public void testRenderInitialBoard() {
    model.startGame();
    output = view.render(model);

    String expected =
            "0 1___1 0\n" +
            "0 1___1 0\n" +
            "0 1___1 0\n";

    Assert.assertEquals(expected, output.toString());
  }

  @Test
  public void testRenderAfterCardPlacement() {
    model.startGame();
    model.placeCard(1, 0, card1);
    output = view.render(model);

    String expected =
            "0 2___1 0\n" +
            "3 R1__1 0\n" +
            "0 2___1 0\n";

    Assert.assertEquals(expected, output.toString());
  }

  @Test
  public void testRenderAfterMultipleMoves() {
    model.startGame();
    model.placeCard(1, 0, card1);
    model.placeCard(2, 4, card2);
    output = view.render(model);

    String expected =
            "0 2___2 0\n" +
            "3 R1__1 0\n" +
            "0 2___B 2\n";

    Assert.assertEquals(expected, output.toString());
  }

  @Test
  public void testRenderFinalGameState() {
    model.startGame();

    model.placeCard(1, 0, card1);
    model.placeCard(2, 4, card2);
    model.placeCard(0, 0, card2);
    model.placeCard(1, 4, card1);
    output = view.render(model);

    String expected =
            "2 R___3 0\n" +
            "3 R1_1B 3\n" +
            "0 3___B 2\n";

    Assert.assertEquals(expected, output.toString());
  }
}