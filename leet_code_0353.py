"""
    请你设计一个 贪吃蛇游戏，该游戏将会在一个 屏幕尺寸 = 宽度 x 高度 的屏幕上运行。如果你不熟悉这个游戏，可以 点击这里 在线试玩。
起初时，蛇在左上角的 (0, 0) 位置，身体长度为 1 个单位。你将会被给出一个数组形式的食物位置序列 food ，其中 food[i] = (ri, ci) 。当蛇吃到
食物时，身子的长度会增加 1 个单位，得分也会 +1 。 食物不会同时出现，会按列表的顺序逐一显示在屏幕上。比方讲，第一个食物被蛇吃掉后，第二个食物才
会出现。当一个食物在屏幕上出现时，保证 不会 出现在被蛇身体占据的格子里。
    如果蛇越界（与边界相撞）或者头与 移动后 的身体相撞（即，身长为 4 的蛇无法与自己相撞），游戏结束。

    实现 SnakeGame 类：
        SnakeGame(int width, int height, int[][] food) 初始化对象，屏幕大小为 height x width ，食物位置序列为 food
        int move(String direction) 返回蛇在方向 direction 上移动后的得分。如果游戏结束，返回 -1 。
"""
import collections
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = collections.deque([(0, 0)])
        self.snake_set = {(0, 0): 1}

        self.width = width
        self.height = height

        self.food = food
        self.food_index = 0

        self.movement = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }

    def move(self, direction: str) -> int:
        new_head = (self.snake[0][0] + self.movement[direction][0], self.snake[0][0] + self.movement[direction][1])

        boundary_1 = new_head[0] < 0 or new_head[0] >= self.height
        boundary_2 = new_head[1] < 0 or new_head[1] >= self.width

        head_3 = new_head in self.snake_set and new_head != self.snake[-1]

        bit_self = boundary_1 or boundary_2 or head_3
        if bit_self:
            return -1

        # 注意，此时食物清单可能是空的。
        next_food_item = self.food[self.food_index] if self.food_index < len(self.food) else None

        # 如果有可用的食物，并且它在移动后蛇占据的单元格上，就吃掉它。
        if next_food_item and next_food_item[0] == new_head[0] and next_food_item[1] == new_head[1]:
            self.food_index += 1
        else:  # 没有吃食物就删掉尾节点
            tail = self.snake.pop()
            del self.snake_set[tail]

        # 总会有新的头节点加入
        self.snake.appendleft(new_head)

        # 也将头部添加到集合中
        self.snake_set[new_head] = 1

        return len(self.snake) - 1
