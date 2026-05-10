def create_Board():
    board = [[-2, -3, -4, -6, -5, -4, -3, -2],
             [-1, -1, -1, -1, -1, -1, -1, -1],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [2, 3, 4, 5, 6, 4, 3, 2]]
    return board
    #0 empty, 1 pawn, 2 rock, 3 bishoop, 4 khingt, 5 queen, 6 king
    # nevatig it's a black, positive number is white
    
FIGURES = {
        1: "♙", 2: "♖", 3: "♘", 4: "♗", 5: "♕", 6: "♔", #white
        -1: "♟", -2: "♜", -3: "♞", -4: "♝", -5: "♛", -6: "♚", # black
        0: ""
    }