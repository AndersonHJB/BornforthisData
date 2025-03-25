/*
 * @Time    : 2025/3/24 14:52
 * @Author  : AI悦创
 * @FileName: StrategyTest.java
 * @Software: IntelliJ IDEA
 * @Version: V1.0
 * @Blog    : https://bornforthis.cn/
 * Code is far away from bugs with the god animal protecting
 * I love animals. They taste delicious.
 */
package cs3500.pawnsboard.strategy;

import cs3500.pawnsboard.model.*;
import cs3500.pawnsboard.model.Board;
import cs3500.pawnsboard.model.Card;
import cs3500.pawnsboard.model.InfluenceGrid;
import cs3500.pawnsboard.model.Player;
import cs3500.pawnsboard.model.Deck;
import java.util.ArrayList;
import java.util.List;

public class StrategyTest {
    public static void main(String[] args) {
        // 创建一个 3x5 的简单棋盘
        IBoard board = new Board(3, 5);

        // 创建一个简单的影响力网格
        String[] gridPattern = {
                "IIIII",
                "IIIII",
                "IIIII",
                "IIIII",
                "IIIII"
        };
        IInfluenceGrid influence = new InfluenceGrid(gridPattern);

        // 创建两个简单的卡牌
        ICard card1 = new Card("Card1", 1, 2, influence);
        ICard card2 = new Card("Card2", 1, 3, influence);

        // 为玩家构造牌组
        List<ICard> redCards = new ArrayList<>();
        redCards.add(card1);
        redCards.add(card2);
        IDeck redDeck = new Deck(redCards);

        List<ICard> blueCards = new ArrayList<>();
        blueCards.add(card1);
        blueCards.add(card2);
        IDeck blueDeck = new Deck(blueCards);

        // 创建玩家（手牌大小为 2），注意玩家名字必须为 "red" 或 "blue" 以便策略判断颜色
        IPlayer redPlayer = new Player("red", redDeck, 2);
        IPlayer bluePlayer = new Player("blue", blueDeck, 2);

        // 创建游戏模型
        IPawnsBoardModel model = new PawnsBoardModelImpl(board, redPlayer, bluePlayer, 2);
        model.startGame();

        // 测试 FillFirstStrategy
        IStrategy fillFirst = new FillFirstStrategy();
        Move move1 = fillFirst.chooseMove(model);
        System.out.println("FillFirstStrategy move: " + move1);

        // 测试 MaximizeRowScoreStrategy
        IStrategy maximizeRow = new MaximizeRowScoreStrategy();
        Move move2 = maximizeRow.chooseMove(model);
        System.out.println("MaximizeRowScoreStrategy move: " + move2);
    }
}

