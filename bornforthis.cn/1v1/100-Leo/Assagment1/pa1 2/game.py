import random
import copy

"""
# Shapes is a 4D list containing the shapes of the 7 pieces
# Each piece contains 4 rotation states
# Each rotation state contains 4 blocks and their relative positions
# DO NOT MODIFY
"""
shapes = [
    # shape 0
    # ****
    [
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[1, 1], [0, 1], [-1, 1], [-2, 1]],
        [[0, 3], [0, 2], [0, 1], [0, 0]],
        [[-2, 1], [-1, 1], [0, 1], [1, 1]],
    ],
    # shape 1
    # **
    # **
    [
        [[0, 0], [0, 1], [1, 0], [1, 1]],
        [[0, 1], [1, 1], [0, 0], [1, 0]],
        [[1, 1], [1, 0], [0, 1], [0, 0]],
        [[1, 0], [0, 0], [1, 1], [0, 1]],
    ],
    # shape 2
    # *
    # ***
    [
        [[0, 0], [1, 0], [1, 1], [1, 2]],
        [[1, 0], [1, 1], [0, 1], [-1, 1]],
        [[1, 2], [0, 2], [0, 1], [0, 0]],
        [[-1, 2], [-1, 1], [0, 1], [1, 1]],
    ],
    # shape 3
    #   *
    # ***
    [
        [[1, 0], [1, 1], [1, 2], [0, 2]],
        [[1, 1], [0, 1], [-1, 1], [-1, 0]],
        [[0, 2], [0, 1], [0, 0], [1, 0]],
        [[-1, 1], [0, 1], [1, 1], [1, 2]],
    ],
    # shape 4
    #  **
    # **
    [
        [[1, 0], [1, 1], [0, 1], [0, 2]],
        [[1, 1], [0, 1], [0, 0], [-1, 0]],
        [[0, 2], [0, 1], [1, 1], [1, 0]],
        [[-1, 0], [0, 0], [0, 1], [1, 1]],
    ],
    # shape 5
    # **
    #  **
    [
        [[0, 0], [0, 1], [1, 1], [1, 2]],
        [[1, 1], [0, 1], [0, 2], [-1, 2]],
        [[1, 2], [1, 1], [0, 1], [0, 0]],
        [[-1, 2], [0, 2], [0, 1], [1, 1]],
    ],
    # shape 6
    #  *
    # ***
    [
        [[0, 1], [1, 0], [1, 1], [1, 2]],
        [[0, 0], [1, 1], [0, 1], [-1, 1]],
        [[1, 1], [0, 2], [0, 1], [0, 0]],
        [[0, 2], [-1, 1], [0, 1], [1, 1]],
    ],
]

ROWS = 20   # number of rows in gameboard
COLS = 6    # number of columns in gamebard
BLOCKS = 4  # number of blocks in a piece

"""
# This function initializes the game board
# It returns a 2D list with 20 rows and 6 columns, all filled with 0, representing the initial empty game board
# You may also modify this function to return other lists for debugging purposes, but please remember to change it back before submitting
# Parameters: None
# Return: 2D list with 20 rows and 6 columns
"""
def init_gameboard():
    """
    # Task 1: Initialize Game Board
    # You have to return a 2D list (a list of lists) with 20 rows and 6 columns, all filled with 0 of type int
    # Please also make sure that each list is independent (having different ids), i.e. changing one list should not affect the others
    """
    ### TASK 1 STARTS HERE ###

    return [[0, 0], [0, 0]]  # this line also need to change
    ### TASK 1 ENDS HERE ###


# This function generates a random number from a list of candidates
# This function is used for generating random values for the blocks
# This function will be used for grading purposes
# Parameters: None
# Return: int, a random number from the list of candidates
def default_random_number_generator():
    """
    # Task 2: Biased Random Value Selection
    # You have been provided with an implementation of a random number generator
    # However, it is not very interesting as it may select some very large numbers (511 and 1023), making the game too easy
    # Your task is to modify this function so that:
    # 1. It only selects numbers [1, 3, 7, 15, 31, 63, 127, 255], i.e. stop generating 511 and 1023.
    # 2. Make the generator favor the generation of smaller numbers. To accomplish this, you should generate 2 numbers randomly each time and return the smaller one.
    """

    ### TASK 2 STARTS HERE ###
    candidates = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]
    index = random.randint(0, len(candidates) - 1)  # Generate random number from 0 to len(candidates) - 1      
    return candidates[index]
    ### TASK 2 ENDS HERE ###

"""
# This function generates a random number from a list of candidates
# This function is used for generating random values for the blocks
# This function will NOT be used for grading purposes
# Feel free to design your own random number generator to make the game more interesting
# Parameters: None
# Return: int, a random number from the list of candidates
"""
def custom_random_number_generator():
    """
    # Optional Task: Custom Random Value Selection ###
    # This task is completely optional and will not be graded
    # You can implement your own random number generator here to make the game more interesting
    # You can use any random number generation technique you like, such as favoring small/large numbers, changing the list of candidates, or any other idea you have
    # You can also use this function to debug your other functions if you want to.
    """
    ### OPTIONAL TASK STARTS HERE ###
    return 1
    ### OPTIONAL TASK ENDS HERE ###

"""
# This function generates a random shape and random block values for the shape
# DO NOT MODIFY THIS FUNCTION
# Parameters: random_number_generator (function), a function that generates a random number, should be either default_random_number_generator or custom_random_number_generator
# Return: current_shape (int), the shape of the current piece
#         block_values (list), the values of the blocks of the current piece, a list of 4 integers
"""
def generate_shape(random_number_generator):
    # DO NOT MODIFY
    current_shape = random.randint(0, len(shapes) - 1)
    block_values = [0, 0, 0, 0]
    for i in range(BLOCKS):
        block_values[i] = random_number_generator()
    return current_shape, block_values

"""
# This function checks if the current move is valid
# More specifically, if the current location and rotation of the current piece
# is valid, i.e. not out of bounds and not overlapping with existing blocks
# Parameters: game_board (2D list), the current game board
#             current_shape (int), the shape of the current piece
#             current_location (list), the row and column of the current piece
#             current_rotation (int), the rotation of the current piece
# Return: bool, True if the move is valid, False otherwise
"""
def is_valid_move(game_board, current_shape, current_location, current_rotation):
    """
    # Task 3: Valid Position Check
    # You have to check if the current location and rotation of the current piece is valid
    # The move is invalid if any of the following conditions occur:
    # 1. Any block of the current piece is out of bounds in any side, revisit task 1 for the board size
    # 2. Any block of the current piece overlaps with an existing block on the game board
    # You have to return True if the move is valid, False otherwise
    """

    ### TASK 3 STARTS HERE ###
    


    return False  # this line also needs to change
    ### TASK 3 ENDS HERE ###

"""
# This function moves the current piece to the left, if the move is valid
# Parameters: game_board (2D list), the current game board
#             current_shape (int), the shape of the current piece
#             current_location (list), the row and column of the current piece
#             current_rotation (int), the rotation of the current piece
# Return: new current location (list), the new row and column of the current piece
#         new current rotation (int), the new rotation of the current piece
"""
def move_left(game_board, current_shape, current_location, current_rotation):
    """
    # Task 4: Move Left
    # You have to move the current piece to the left by 1 block if the move is valid
    # Keep the positions unchanged if the move is invalid
    # You may want to use the is_valid_move function to check if the move is valid
    # You have to return the new location and rotation of the current piece
    """

    ### TASK 4 STARTS HERE ###
    

    return [0, 0], 0 # this line also needs to change
    ### TASK 4 ENDS HERE ###

"""
# This function moves the current piece to the right, if the move is valid
# Parameters: game_board (2D list), the current game board
#             current_shape (int), the shape of the current piece
#             current_location (list), the row and column of the current piece
#             current_rotation (int), the rotation of the current piece
# Return: new current location (list), the new row and column of the current piece
#         new current rotation (int), the new rotation of the current piece
"""
def move_right(game_board, current_shape, current_location, current_rotation):
    """
    # Task 5: Move Right
    # You have to move the current piece to the right by 1 block if the move is valid
    # Keep the positions unchanged if the move is invalid
    # You may want to use the is_valid_move function to check if the move is valid
    # You have to return the new location and rotation of the current piece
    """

    ### TASK 5 STARTS HERE ###
    
    return [0, 0], 0 # this line also needs to change
    ### TASK 5 ENDS HERE ###

"""
# This function moves the current piece down, if the move is valid
# Parameters: game_board (2D list), the current game board
#             current_shape (int), the shape of the current piece
#             current_location (list), the row and column of the current piece
#             current_rotation (int), the rotation of the current piece
# Return: new current location (list), the new row and column of the current piece
#         new current rotation (int), the new rotation of the current piece
"""
def move_down(game_board, current_shape, current_location, current_rotation):
    """
    # Task 6: Move Down
    # You have to move the current piece down by 1 block if the move is valid
    # Keep the positions unchanged if the move is invalid
    # You may want to use the is_valid_move function to check if the move is valid
    # You have to return the new location and rotation of the current piece
    """

    ### TASK 6 STARTS HERE ###
    
    

    return [0, 0], 0  # change this line
    ### TASK 6 ENDS HERE ###

"""
# This function rotates the current piece, if the move is valid
# Parameters: game_board (2D list), the current game board
#             current_shape (int), the shape of the current piece
#             current_location (list), the row and column of the current piece
#             current_rotation (int), the rotation of the current piece
# Return: new current location (list), the new row and column of the current piece
#         new current rotation (int), the new rotation of the current piece
"""
def rotate(game_board, current_shape, current_location, current_rotation):
    """
    # Task 7: Rotate Piece
    # You have to rotate the current piece if the move is valid
    # Recall that rotations are stored with the current_rotation variable and with the transition
    # 0 --rotation-> 1 --rotation-> 2 --rotation-> 3 --rotation-> 0
    # Keep the positions unchanged if the move is invalid
    # You may want to use the is_valid_move function to check if the move is valid
    # You have to return the new location and rotation of the current piece
    # You are required to keep the current_rotation within {0, 1, 2, 3}.
    """

    ### TASK 7 STARTS HERE ###
    
    return [0, 0], 0  # change this line
    ### TASK 7 ENDS HERE ###

"""
# This functions processes both the gravity and the merging of the blocks on the game board
# The gravity moves the blocks down as far as possible
# The merging merges the blocks that have the same value and are stacking vertically
# Keep the process until no more merging can be done, and no more blocks are floating in the air
# Parameters: game_board (2D list), the current game board, possibly with floating blocks
# Return: None
"""
def gravity_and_merge(game_board):
    """
    # Task 8: Gravity and Merge
    # You have to implement the gravity and merging of the blocks on the game board
    # The gravity moves the blocks down as far as possible and works on each individual block by turn, not the entire piece at the same time
    # The merging merges the blocks that have the same value and are stacking vertically
    # Keep the process until no more merging can be done, and no more blocks are floating in the air
    # Keep merging the bottommost pair of blocks with the same value, that is to say, begin merging checks from bottom up, not top down
    """

    ### TASK 8 STARTS HERE ###
   
   
    pass
    ### TASK 8 ENDS HERE ###

"""
# This function checks if the game is over
# The player loses if there is any block on the first 5 rows of the game board, return "Lose"
# The player wins if there is a block with value exactly 1023 on the game board, return "Win"
# If the player satisfies both conditions at the same time, the player still count as losing, return "Lose"
# If neither of the above conditions are met, return "Playing"
# Parameters: game_board (2D list), the current game board
# Return: str, the status of the game, either "Win", "Lose", or "Playing"
"""
def get_game_status(game_board):
    """
    # Task 9: Get Game Status
    # Complete the get_game_status function according to the function description above
    """

    ### TASK 9 STARTS HERE ###
    


    return "Playing"
    ### TASK 9 ENDS HERE ###
