# You do not need to submit this file
# Feel free to modify this file to customize the game and test your implementation

import tkinter as tk
from game import (
    init_gameboard,
    generate_shape,
    move_left,
    move_right,
    move_down,
    rotate,
    gravity_and_merge,
    get_game_status,
    default_random_number_generator,
    custom_random_number_generator,
    shapes,
)

# The random number generator, feel free to change this to custom_random_number_generator for self testing/fun
generator = default_random_number_generator

# The colors for the blocks
colors = {
    1: "#ebdfc7",
    3: "#f1ae77",
    7: "#f59460",
    15: "#f37b5d",
    31: "#f45e3b",
    63: "#ebcc71",
    127: "#ebca5f",
    255: "#ebc74f",
    511: "#ebc340",
    1023: "#ecc02c",
}


# A class to represent the GUI
# Don't worry if you don't understand about class yet. This file does not require submission and is purely for visual display and interactivity.
class GUI:
    # Constructor of the GUI class
    # Will be called once when app = GUI(root) is run
    # Parameters: root - the root window of the GUI, which is created using tk.Tk()
    def __init__(self, root):
        self.root = root
        self.root.title("1023 Game")
        self.canvas = tk.Canvas(root, width=500, height=600, bg="white")
        self.canvas.pack()
        self.game_board = init_gameboard()
        self.current_shape, self.block_values = generate_shape(generator)
        self.current_rotation = 0
        self.current_location = [0, 1]
        self.status = "Playing"
        self.draw_board()
        self.root.bind("<Key>", self.key_pressed)

    # Function to draw the game result on the canvas
    # Parameters: None
    # Returns: None
    def draw_results(self):
        if self.status == "Win":
            self.canvas.create_text(
                400, 100, text="You win!", font=("Helvetica", 20), fill="green"
            )
            return
        elif self.status == "Lose":
            self.canvas.create_text(
                400, 100, text="You lose!", font=("Helvetica", 20), fill="red"
            )
            return

    # Function to draw the game board on the canvas
    # Parameters: None
    # Returns: None
    def draw_board(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_results()
        for i, row in enumerate(self.game_board):
            for j, val in enumerate(row):
                if val != 0:
                    self.draw_block(i, j, val)
        if self.current_shape != -1:
            for i in range(4):
                row = (
                    self.current_location[0]
                    + shapes[self.current_shape][self.current_rotation][i][0]
                )
                col = (
                    self.current_location[1]
                    + shapes[self.current_shape][self.current_rotation][i][1]
                )
                self.draw_block(row, col, self.block_values[i])

    # Function to draw the grid on the canvas
    # Parameters: None
    # Returns: None
    def draw_grid(self):
        self.canvas.create_rectangle(0, 0, 300, 600, fill="#d1c3b6")
        for i in range(21):
            self.canvas.create_line(0, i * 30, 300, i * 30)
        for i in range(7):
            self.canvas.create_line(i * 50, 0, i * 50, 600)
        self.canvas.create_line(0, 120, 300, 120, width=2, fill="red")

    # Function to draw a block on the canvas
    # Parameters: row - the row of the block, col - the column of the block, val - the value of the block
    # Returns: None
    def draw_block(self, row, col, val):
        x0 = col * 50
        y0 = row * 30
        x1 = x0 + 50
        y1 = y0 + 30
        fill = "#efe5db"
        if val in colors.keys():
            fill = colors[val]
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline="black")
        text_color = "white"
        if val == 1 or val not in colors.keys():
            text_color = "black"
        self.canvas.create_text(x0 + 25, y0 + 15, text=str(val), fill=text_color)

    # Function to handle key press events
    # Will be called everytime a key is pressed
    # Similar to the main function in the cli.py file
    # Parameters: event - the key press event
    def key_pressed(self, event):
        key = event.keysym
        if key == "q":
            self.root.quit()
        elif key == "a" or key == "Left":
            if self.status == "Playing":
                self.current_location, self.current_rotation = move_left(
                    self.game_board,
                    self.current_shape,
                    self.current_location,
                    self.current_rotation,
                )
        elif key == "d" or key == "Right":
            if self.status == "Playing":
                self.current_location, self.current_rotation = move_right(
                    self.game_board,
                    self.current_shape,
                    self.current_location,
                    self.current_rotation,
                )
        elif key == "s" or key == "Down":
            if self.status == "Playing":
                self.current_location, self.current_rotation = move_down(
                    self.game_board,
                    self.current_shape,
                    self.current_location,
                    self.current_rotation,
                )
        elif key == "w" or key == "Up":
            if self.status == "Playing":
                self.current_location, self.current_rotation = rotate(
                    self.game_board,
                    self.current_shape,
                    self.current_location,
                    self.current_rotation,
                )
        elif key == "space":
            if self.status == "Playing":
                for i in range(4):
                    row = (
                        self.current_location[0]
                        + shapes[self.current_shape][self.current_rotation][i][0]
                    )

                    col = (
                        self.current_location[1]
                        + shapes[self.current_shape][self.current_rotation][i][1]
                    )

                    self.game_board[row][col] = self.block_values[i]
                gravity_and_merge(self.game_board)
                self.current_shape = -1
                self.status = get_game_status(self.game_board)
                if self.status == "Win":
                    self.draw_board()
                    return
                elif self.status == "Lose":
                    self.draw_board()
                    return
                self.current_shape, self.block_values = generate_shape(generator)
                self.current_rotation = 0
                self.current_location = [0, 1]
        self.draw_board()


# The main function to run the GUI
# When this file is run directly, the GUI version of the game will start
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
