# You do not need to submit this file
# Feel free to modify this file to customize the game and test your implementation

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


# This function prints the game board to the console
# Parameters: game_board (2D list)
#             current_shape (int), the shape of the current piece, -1 if no shape (e.g. when game ends) (default -1)
#             current_location (list), the row and column of the current piece (default [0, 0])
#             current_rotation (int), the rotation of the current piece (default 0)
#             block_values (list), the values of the blocks of the current piece (default [0, 0, 0, 0])
# Return: None
def print_gameboard(
    game_board,
    current_shape=-1,
    current_location=[0, 0],
    current_rotation=0,
    block_values=[0, 0, 0, 0],
):
    printing_board = []
    for i in range(20):
        printing_board.append(list(game_board[i]))
    if current_shape != -1:
        for i in range(4):
            row = current_location[0] + shapes[current_shape][current_rotation][i][0]
            col = current_location[1] + shapes[current_shape][current_rotation][i][1]
            printing_board[row][col] = block_values[i]
    for i, row in enumerate(printing_board):
        for col in row:
            print(str(col).rjust(4), end=" ")
        print()
        if i == 3:
            print("-" * 29)


# This is the main function that runs the game
# Feel free to modify this function. It will not be graded.
# Parameters: None
# Return: None
def main():
    ### Modify the generator to custom_random_number_generator if you want to run your custom random number generator instead.
    generator = default_random_number_generator
    game_board = init_gameboard()
    current_shape, block_values = generate_shape(generator)
    current_rotation = 0
    current_location = [0, 1]
    while True:
        print_gameboard(
            game_board, current_shape, current_location, current_rotation, block_values
        )
        key = input("Key: ")
        if len(key) > 1:
            key = key[0]
        if key == "q":
            break
        elif key == "a":
            current_location, current_rotation = move_left(
                game_board, current_shape, current_location, current_rotation
            )
        elif key == "d":
            current_location, current_rotation = move_right(
                game_board, current_shape, current_location, current_rotation
            )
        elif key == "s":
            current_location, current_rotation = move_down(
                game_board, current_shape, current_location, current_rotation
            )
        elif key == "w":
            current_location, current_rotation = rotate(
                game_board, current_shape, current_location, current_rotation
            )
        else:
            for i in range(4):
                row = (
                    current_location[0] + shapes[current_shape][current_rotation][i][0]
                )

                col = (
                    current_location[1] + shapes[current_shape][current_rotation][i][1]
                )

                game_board[row][col] = block_values[i]
            gravity_and_merge(game_board)
            current_shape = -1
            status = get_game_status(game_board)
            if status == "Win":
                print("You Win!")
                print_gameboard(game_board)
                break
            elif status == "Lose":
                print("You Lose!")
                print_gameboard(game_board)
                break
            current_shape, block_values = generate_shape(generator)
            current_rotation = 0
            current_location = [0, 1]


# This line is used to call the main function
# When this file is run directly, the console version of the game will start
if __name__ == "__main__":
    main()
