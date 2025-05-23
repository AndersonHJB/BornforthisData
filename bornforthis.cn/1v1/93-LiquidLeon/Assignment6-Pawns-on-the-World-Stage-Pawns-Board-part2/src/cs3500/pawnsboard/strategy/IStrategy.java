/*
 * @Time    : 2025/3/24 14:28
 * @Author  : AI悦创
 * @FileName: IStrategy.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package cs3500.pawnsboard.strategy;
import cs3500.pawnsboard.model.IReadonlyPawnsBoardModel;

public interface IStrategy {
    Move chooseMove(IReadonlyPawnsBoardModel model);
}
