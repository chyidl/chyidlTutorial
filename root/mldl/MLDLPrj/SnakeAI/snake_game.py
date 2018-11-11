#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
curses -- Terminal hamdling for character-cell displays
"""
import curses
from random import randint


class SnakeGame:
    """Snake Game by Python Language"""

    def __init__(self, board_width=20, board_height=20, gui=False):
        self.win = None
        self.food = []
        self.snake = []
        self.score = 0
        self.done = False
        self.board = {'width': board_width, 'height': board_height}
        self.gui = gui

    def start(self):
        """Game Start"""
        self.snake_init()
        self.generate_food()
        if self.gui:
            self.render_init()
        return self.generate_observations()

    def snake_init(self):
        """Snake init"""
        x = randint(5, self.board["width"] - 5)  # randint(a,b) -- Return a random integer N such that a <= N <= b
        y = randint(5, self.board["height"] - 5)
        vertical = randint(0, 1) == 0            # What's this sentence???
        for i in range(3):
            point = [x + i, y] if vertical else [x, y + i]
            self.snake.insert(0, point)          # s.insert(i,x) -- inserts x into s at the index given by i

    def generate_food(self):
        self.food = []
        while not self.food:
            self.food = [randint(1, self.board["width"]), randint(1, self.board["height"])]
            if self.food in self.snake:
                self.food = []

    def render_init(self):
        curses.initscr() # Initialize the library. Return a window object which represents the whole screen.
        self.win = curses.newwin(self.board["width"] + 2, self.board["height"] + 2, 0, 0) # return a new window
        curses.curs_set(0)
        self.win.nodelay(1) # window.nodelay(flag) -- If flag is True, getch() will be non-blocking.
        self.win.timeout(200)
        self.render()

    def render(self):
        self.win.clear()
        self.win.border(0)
        self.win.addstr(0, 2, 'Score : ' + str(self.score) + ' ')
        self.win.addch(self.food[0], self.food[1], '🍎')
        for i, point in enumerate(self.snake):
            if i == 0:
                self.win.addch(point[0], point[1], '🔸')
            else:
                self.win.addch(point[0], point[1], '🔹')
        self.win.getch()

    def step(self, key):
        # 0 - UP
        # 1 - RIGHT
        # 2 - DOWN
        # 3 - LEFT
        if self.done:
            self.end_game()
        self.create_new_point(key)
        if self.food_eaten():
            self.score += 1
            self.generate_food()
        else:
            self.remove_last_point()
        self.check_collisions()
        if self.gui:
            self.render()
        return self.generate_observations()

    def create_new_point(self, key):
        new_point = [self.snake[0][0], self.snake[0][1]]
        if key == 0:    # UP
            new_point[0] -= 1
        elif key == 1:  # RIGHT
            new_point[1] += 1
        elif key == 2:  # DOWN
            new_point[0] += 1
        elif key == 3:  # LEFT
            new_point[1] -= 1
        self.snake.insert(0, new_point)

    def remove_last_point(self):
        self.snake.pop()

    def food_eaten(self):
        return self.snake[0] == self.food

    def check_collisions(self):
        if (self.snake[0][0] == 0 or
                self.snake[0][0] == self.board["width"] + 1 or
                self.snake[0][1] == 0 or
                self.snake[0][1] == self.board["height"] + 1 or
                self.snake[0] in self.snake[1:-1]):
            self.done = True

    def generate_observations(self):
        return self.done, self.score, self.snake, self.food

    def render_destroy(self):
        curses.endwin()

    def end_game(self):
        if self.gui:
            self.render_destroy()
        raise Exception("Game Over")


if __name__ == "__main__":
    game = SnakeGame(gui=True)
    game.start()
    for _ in range(200):
        game.step(randint(0, 3))
