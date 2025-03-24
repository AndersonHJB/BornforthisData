/*
 * @Time    : 2025/3/24 13:34
 * @Author  : AI悦创
 * @FileName: IReadOnlyPawnsBoardModel.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package cs3500.pawnsboard.model;

public interface IReadonlyPawnsBoardModel {

    GameState getGameState();

    IBoard getBoard();

    IPlayer getCurrentPlayer();

    boolean isLegalMove(int x, int y, ICard card);
}
