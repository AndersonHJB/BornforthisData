package cs3500.pawnsboard.model;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Reads a deck configuration file and creates a list of cards.
 */
public class DeckReader {

  /**
   * Reads a deck configuration file and returns two decks of carrd.
   * One for red and one for blue player.
   * @param filePath the path to the deck configuration file.
   * @return a list of decks containing the cards for each player.
   * @throws FileNotFoundException if the file is not found
   * @throws IllegalArgumentException if the file format is invalid
   */
  public static List<ICard>[] readDeckFile(String filePath) throws FileNotFoundException {
    List<ICard> redDeck = new ArrayList<>();
    List<ICard> blueDeck = new ArrayList<>();
    File file = new File(filePath);
    Scanner scan = new Scanner(file);
    while (scan.hasNextLine()) {
      try {
        String[] firstLine = scan.nextLine().split(" ");
        if (firstLine.length != 3) {
          throw new IllegalArgumentException("Invalid format: missing name cost value");
        }
        String name = firstLine[0];
        int cost = Integer.parseInt(firstLine[1]);
        int value = Integer.parseInt(firstLine[2]);
        String[] influenceContentRed = new String[5];
        String[] influenceContentBlue = new String[5];
        for (int i = 0; i < 5; i++) {
          if (!scan.hasNextLine()) {
            throw new IllegalArgumentException("Invalid format: influence grid incomplete");
          }
          String row = scan.nextLine();
          if (row.length() != 5) {
            throw new IllegalArgumentException("Invalid format: row not 5 characters long");
          }
          influenceContentRed[i] = row;
          influenceContentBlue[i] = new StringBuilder(row).reverse().toString();
        }
        IInfluenceGrid redGrid = new InfluenceGrid(influenceContentRed);
        IInfluenceGrid blueGrid = new InfluenceGrid(influenceContentBlue);
        ICard redCard = new Card(name, cost, value, redGrid);
        ICard blueCard = new Card(name, cost, value, blueGrid);
        redDeck.add(redCard);
        blueDeck.add(blueCard);
      } catch (NumberFormatException e) {
        throw new IllegalArgumentException("Invalid format: cost and value");
      }
    }
    scan.close();
    return new List[]{redDeck, blueDeck};
  }
}
