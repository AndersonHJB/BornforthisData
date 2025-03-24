/*
 * @Time    : 2025/3/24 14:45
 * @Author  : AI悦创
 * @FileName: FillFirstStrategy.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package cs3500.pawnsboard.strategy;

import cs3500.pawnsboard.model.IReadonlyPawnsBoardModel;
import cs3500.pawnsboard.model.ICard;
import cs3500.pawnsboard.model.IBoard;
import cs3500.pawnsboard.model.IPlayer;

public class FillFirstStrategy implements IStrategy {

    @Override
    public Move chooseMove(IReadonlyPawnsBoardModel model) {
        IPlayer currentPlayer = model.getCurrentPlayer();
        IBoard board = model.getBoard();
        for (int cardIndex = 0; cardIndex < currentPlayer.getHand().size(); cardIndex++) {
            ICard card = currentPlayer.getHand().get(cardIndex);
            for (int row = 0; row < board.getRows(); row++) {
                for (int col = 0; col < board.getCols(); col++) {
                    if (model.isLegalMove(row, col, card)) {
                        return Move.placementMove(cardIndex, row, col);
                    }
                }
            }
        }
        return Move.pass();
    }
}
