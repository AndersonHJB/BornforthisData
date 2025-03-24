package cs3500.pawnsboard;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;

import cs3500.pawnsboard.model.Board;
import cs3500.pawnsboard.model.Deck;
import cs3500.pawnsboard.model.DeckReader;
import cs3500.pawnsboard.model.IBoard;
import cs3500.pawnsboard.model.ICard;
import cs3500.pawnsboard.model.IDeck;
import cs3500.pawnsboard.model.IPawnsBoardModel;
import cs3500.pawnsboard.model.IPlayer;
import cs3500.pawnsboard.model.PawnsBoardModelImpl;
import cs3500.pawnsboard.model.Player;
import cs3500.pawnsboard.view.TextualPawnsBoardView;

/**
 * Entry point for the Pawns Board game.
 * Reads a deck configuration file, initializes the game, and runs a
 * sample game.
 */
public class PawnsBoardGame {
  /**
   * Main Method.
   * @param args inputs
   */
  public static void main(String[] args) {
    String filePath = "Assignment05" + File.separator
            + "docs" + File.separator + "deck.config";
    List<ICard>[] decks;
    try {
      decks = DeckReader.readDeckFile(filePath);
    } catch (FileNotFoundException e) {
      System.out.println("File not found");
      return;
    } catch (IllegalArgumentException e) {
      System.out.println("Invalid format");
      return;
    }
    IDeck redDeck = new Deck(decks[0]);
    IDeck blueDeck = new Deck(decks[1]);
    IPlayer redPlayer = new Player("red", redDeck, 5);
    IPlayer bluePlayer = new Player("blue", blueDeck, 5);
    IBoard board = new Board(3, 5);
    IPawnsBoardModel model = new PawnsBoardModelImpl(board, redPlayer, bluePlayer, 5);
    TextualPawnsBoardView view = new TextualPawnsBoardView();

    model.startGame();
    view.printBoard(model);
    model.placeCard(1,0,redPlayer.getHand().get(0));
    view.printBoard(model);
    model.placeCard(2,4,bluePlayer.getHand().get(1));
    view.printBoard(model);
    model.passTurn();
    view.printBoard(model);
    model.placeCard(0,4,bluePlayer.getHand().get(0));
    view.printBoard(model);
    model.placeCard(0,0,redPlayer.getHand().get(0));
    view.printBoard(model);
    model.placeCard(1,4,bluePlayer.getHand().get(0));
    view.printBoard(model);
    model.placeCard(2,0,redPlayer.getHand().get(0));
    view.printBoard(model);
    model.placeCard(0,3,bluePlayer.getHand().get(2));
    view.printBoard(model);
    model.placeCard(1,1,redPlayer.getHand().get(2));
    view.printBoard(model);
    model.placeCard(1,3,bluePlayer.getHand().get(4));
    view.printBoard(model);
    model.placeCard(2,1,redPlayer.getHand().get(2));
    view.printBoard(model);
    model.passTurn();
    model.placeCard(0,1,redPlayer.getHand().get(3));
    view.printBoard(model);
    System.out.println("Game Over: " + model.getGameState());
  }
}
