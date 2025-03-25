/*
 * @Time    : 2025/3/24 14:52
 * @Author  : AI悦创
 * @FileName: MaximizeRowScoreStrategy.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package cs3500.pawnsboard.strategy;

import cs3500.pawnsboard.model.IReadonlyPawnsBoardModel;
import cs3500.pawnsboard.model.IBoard;
import cs3500.pawnsboard.model.IPlayer;
import cs3500.pawnsboard.model.ICard;

public class MaximizeRowScoreStrategy implements IStrategy {

    @Override
    public Move chooseMove(IReadonlyPawnsBoardModel model) {
        IPlayer currentPlayer = model.getCurrentPlayer();
        // 通过玩家名字判断颜色（约定：名字为 "red" 表示红方）
        boolean currentIsRed = currentPlayer.getName().equalsIgnoreCase("red");
        IBoard board = model.getBoard();
        int rows = board.getRows();
        int cols = board.getCols();

        // 自顶向下逐行检查
        for (int row = 0; row < rows; row++) {
            // 计算当前行中双方的得分
            int currentScore = calculateRowScore(board, row, currentIsRed);
            int opponentScore = calculateRowScore(board, row, !currentIsRed);

            // 若当前玩家得分小于或等于对手，则尝试寻找一个能使得分超过对手的下法
            if (currentScore <= opponentScore) {
                for (int cardIndex = 0; cardIndex < currentPlayer.getHand().size(); cardIndex++) {
                    ICard card = currentPlayer.getHand().get(cardIndex);
                    // 只考虑在该行的下法
                    for (int col = 0; col < cols; col++) {
                        if (model.isLegalMove(row, col, card)) {
                            int newScore = currentScore + card.getValue();
                            if (newScore > opponentScore) {
                                return Move.placementMove(cardIndex, row, col);
                            }
                        }
                    }
                }
            }
        }
        // 若没有合适的下法，则 pass
        return Move.pass();
    }

    /**
     * 计算指定行中某一方的得分（仅统计已下卡牌的价值）。
     * @param board 棋盘
     * @param row 行号
     * @param isRed true 表示红方，false 表示蓝方
     * @return 该行的总得分
     */
    private int calculateRowScore(IBoard board, int row, boolean isRed) {
        int score = 0;
        for (int col = 0; col < board.getCols(); col++) {
            if (board.getCell(row, col).hasCard() &&
                    board.getCell(row, col).isOwnedByRed() == isRed) {
                score += board.getCell(row, col).getCard().getValue();
            }
        }
        return score;
    }
}

