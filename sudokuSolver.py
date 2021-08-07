
# Length of board is 9

board = [
    [0, 0, 0, 0, 0, 0, 0, 7, 9],
    [8, 0, 5, 0, 7, 4, 1, 0, 0],
    [4, 6, 0, 1, 0, 0, 0, 3, 8],
    [0, 0, 0, 6, 5, 0, 9, 1, 0],
    [0, 0, 6, 9, 1, 7, 0, 0, 4],
    [0, 1, 9, 4, 3, 2, 0, 8, 7],
    [0, 0, 8, 2, 0, 6, 0, 4, 0],
    [6, 0, 2, 0, 0, 0, 0, 9, 1],
    [0, 0, 0, 5, 0, 0, 0, 0, 6]        
]



def print_board(currBoard):
    for i in range(len(currBoard)): 
        if i % 3 == 0 and i != 0:
            print("---------------------")
            # print("_____________________")
        for j in range(len(currBoard[0])):

            if j % 3 == 0 and j != 0:
                print("|", end= " ")

            print(str(currBoard[i][j]) + " ", end = "")
        print()

def find_solution():
    return 1


def is_Valid():
    return 1
