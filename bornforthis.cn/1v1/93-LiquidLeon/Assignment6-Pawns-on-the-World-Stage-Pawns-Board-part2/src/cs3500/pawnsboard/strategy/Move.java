/*
 * @Time    : 2025/3/24 14:31
 * @Author  : AI悦创
 * @FileName: Move.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */

package cs3500.pawnsboard.strategy;

public class Move {
    private final boolean isPass;
    private final int cardIndex;
    private final int row;
    private final int col;

    private Move(boolean isPass, int cardIndex, int row, int col) {
        this.isPass = isPass;
        this.cardIndex = cardIndex;
        this.row = row;
        this.col = col;
    }


    public static Move placementMove(int cardIndex, int row, int col) {
        return new Move(false, cardIndex, row, col);
    }

    public static Move pass() {
        return new Move(true, -1, -1, -1);
    }

    public boolean isPass() {
        return isPass;
    }

    public int getCardIndex() {
        return cardIndex;
    }

    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }

    @Override
    public String toString() {
        if (isPass) {
            return "Pass";
        } else {
            return "Place card at index " + cardIndex + " on (" + row + ", " + col + ")";
        }
    }
}

