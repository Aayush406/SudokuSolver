# board = [
#     [0, 0, 0, 0, 0, 0, 0, 7, 9],
#     [8, 0, 5, 0, 7, 4, 1, 0, 0],
#     [4, 6, 0, 1, 0, 0, 0, 3, 8],
#     [0, 0, 0, 6, 5, 0, 9, 1, 0],
#     [0, 0, 6, 9, 1, 7, 0, 0, 4],
#     [0, 1, 9, 4, 3, 2, 0, 8, 7],
#     [0, 0, 8, 2, 0, 6, 0, 4, 0],
#     [6, 0, 2, 0, 0, 0, 0, 9, 1],
#     [0, 0, 0, 5, 0, 0, 0, 0, 6]        
# ]

# board = [
#     [0, 8, 0, 3, 7, 0, 0, 0, 0],
#     [0, 0, 3, 0, 0, 0, 0, 0, 0],
#     [0, 0, 7, 0, 4, 0, 2, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 8],
#     [0, 0, 0, 0, 0, 0, 4, 3, 7],
#     [8, 0, 9, 0, 0, 0, 0, 0, 2],
#     [0, 0, 0, 8, 0, 0, 6, 0, 0],
#     [5, 6, 0, 0, 0, 9, 0, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 4, 0]        
# ]

# board = [
#     [4, 0, 0, 0, 5, 0, 8, 0, 0],
#     [0, 1, 8, 0, 0, 0, 7, 0, 0],
#     [0, 0, 3, 0, 0, 4, 0, 0, 0],
#     [9, 6, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 5, 0, 0, 3, 0, 0, 0],
#     [0, 7, 0, 0, 0, 8, 0, 6, 0],
#     [0, 0, 1, 6, 0, 0, 0, 0, 4],
#     [0, 0, 0, 5, 0, 0, 0, 1, 3],
#     [0, 0, 0, 8, 0, 0, 0, 0, 0]        
# ]


board = [
        [6, 4, 0, 0, 3, 0, 0, 0, 7],
        [5, 0, 1, 0, 7, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 4, 9, 0, 8, 0, 6, 0],
        [0, 8, 0, 0, 0, 3, 0, 2, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [4, 0, 0, 1, 5, 7, 0, 3, 0],
        [2, 0, 8, 3, 0, 0, 0, 0, 0],
        [7, 5, 0, 0, 0, 0, 0, 9, 6]        
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
        

def find_solution(board):
    empty_spot = findEmptySquare(board)
    if(empty_spot[0] == "Complete"):
        return True

    for num in range(1, 10):
        if (check_spot(board, empty_spot[0], empty_spot[1], num) == True):
            board[empty_spot[0]][empty_spot[1]] = num
            if (find_solution(board) == True):
                return True
        board[empty_spot[0]][empty_spot[1]] = 0
    return False
        

def check_spot(currBoard, currRow, currCol, num):

    for col in range(0, 9): # Check if the value is valid in the current Row
        if(col != currCol):
            if(currBoard[currRow][col] == num):
                return False
    
    for row in range(0,9): # Check if value is correct in current Column
        if(row != currRow):
            if(currBoard[row][currCol] == num):
                return False

    # Check if the value is allowed in the 3 x 3 box 
    startRowSpot = currRow - currRow % 3
    startColSpot = currCol - currCol % 3
    
    for rowInc in range(3):
        for colInc in range(3):
            if (startRowSpot + rowInc != currRow and startColSpot + colInc != currCol):
                if(currBoard[startRowSpot + rowInc][startColSpot + colInc] == num):
                    return False
    
    return True # This is a valid position

    
def findEmptySquare(currBoard): #Finds the next empty spot in the sudoku board and returns whether it exists
    for row in range(9):
        for col in range(9):
            if(currBoard[row][col] == 0):
                return [row, col]
    return ["Complete"] # If the Board is complete



# print_board(board)
# find_solution(board)
# print("++++++++++++++++++++++++++++")
# print_board(board)