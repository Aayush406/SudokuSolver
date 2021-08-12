import pygame
import sudokuSolver


_FRAME_RATE = 10
pygame.init()
pygame.font.init()

class SudokuGrid:


    def __init__(self):
        self._SCREEN_HEIGHT = 800
        self._SCREEN_WIDTH = 800
        self._running = True
        self._seperation_distance = self._SCREEN_WIDTH / 9
        self._font = pygame.font.SysFont("arial", 50)
        self._smaller_font = pygame.font.SysFont("arial", 30)
        self._mouseX = 0
        self._mouseY = 0
        self._mouseClicked = False
        self._insertVal = 0
        self._done = False
        self._once = False 
        self._autoSolve = False
        self._solved = False
        self._board = [
                        [0, 8, 0, 3, 7, 0, 0, 0, 0],
                        [0, 0, 3, 0, 0, 0, 0, 0, 0],
                        [0, 0, 7, 0, 4, 0, 2, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 8],
                        [0, 0, 0, 0, 0, 0, 4, 3, 7],
                        [8, 0, 9, 0, 0, 0, 0, 0, 2],
                        [0, 0, 0, 8, 0, 0, 6, 0, 0],
                        [5, 6, 0, 0, 0, 9, 0, 0, 0],
                        [0, 0, 0, 0, 0, 2, 0, 4, 0]        
                    ]
        self._og_board = [
                            [0, 8, 0, 3, 7, 0, 0, 0, 0],
                            [0, 0, 3, 0, 0, 0, 0, 0, 0],
                            [0, 0, 7, 0, 4, 0, 2, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0, 8],
                            [0, 0, 0, 0, 0, 0, 4, 3, 7],
                            [8, 0, 9, 0, 0, 0, 0, 0, 2],
                            [0, 0, 0, 8, 0, 0, 6, 0, 0],
                            [5, 6, 0, 0, 0, 9, 0, 0, 0],
                            [0, 0, 0, 0, 0, 2, 0, 4, 0]        
                        ]
        
        self._solvedBoard = [
                        [0, 8, 0, 3, 7, 0, 0, 0, 0],
                        [0, 0, 3, 0, 0, 0, 0, 0, 0],
                        [0, 0, 7, 0, 4, 0, 2, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 8],
                        [0, 0, 0, 0, 0, 0, 4, 3, 7],
                        [8, 0, 9, 0, 0, 0, 0, 0, 2],
                        [0, 0, 0, 8, 0, 0, 6, 0, 0],
                        [5, 6, 0, 0, 0, 9, 0, 0, 0],
                        [0, 0, 0, 0, 0, 2, 0, 4, 0]        
                    ]
        sudokuSolver.find_solution(self._solvedBoard)


    def run(self):
 

        try:
            # clock = pygame.time.Clock()
            self._create_surface((self._SCREEN_WIDTH, self._SCREEN_HEIGHT))
            
            
            while self._running:


                self._surface.fill((255,255,255))

                if(self._mouseClicked == True):
                    self._displayCurrentBox()
                
                

                self._draw_lines()
                self._draw_nums()
                self._handle_events()
                # self._displayCurrentBox()
                
                if self._done == True and self._autoSolve == False:
                    self._mark_win()

                pygame.display.flip()


        
        finally:
            pygame.quit()
    


    def _reset_board(self, board1, board2):
        for row in range(len(board1)):
            for col in range(len(board1[row])):
                board1[row][col] = board2[row][col]


    def _check_win(self):
        # if(self._solved == False):
        #     sudokuSolver.find_solution(self._solvedBoard)
        #     self._solved = True

        for row in range(len(self._board)):
            for col in range(len(self._board[0])):
                if(self._board[row][col] != self._solvedBoard[row][col]):
                    self._done = False
                    return
        self._done = True
        return 

    def _check_filled(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                if(self._board[i][j] == 0):
                    return False
        return True


    def _mark_win(self):
        pygame.draw.rect(self._surface, (124, 252, 0), (0,0,self._SCREEN_WIDTH, 34))
        text = self._smaller_font.render("YOU WIN!!!", True, (255,0,0))
        self._surface.blit(text, (350, 0))


    def _draw_lines(self):
        for i in range(10):
            if(i % 3 == 0):
                pygame.draw.line(self._surface, (0, 0, 0), (0, i*self._seperation_distance), (self._SCREEN_WIDTH, i * self._seperation_distance), 8)
                pygame.draw.line(self._surface, (0, 0, 0), (i * self._seperation_distance, 0), (i * self._seperation_distance, self._SCREEN_HEIGHT), 8)
            else:
                pygame.draw.line(self._surface, (0, 0, 0), (0, i*self._seperation_distance), (self._SCREEN_WIDTH, i * self._seperation_distance), 3)
                pygame.draw.line(self._surface, (0, 0, 0), (i * self._seperation_distance, 0), (i * self._seperation_distance, self._SCREEN_HEIGHT), 3)
        
            

    def _draw_nums(self):
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if(self._board[row][col] != 0 and self._og_board[row][col] == 0):
                    text = self._font.render(str(self._board[row][col]), True, (0,0,0))
                    self._surface.blit(text, (col * self._seperation_distance + 34, row * self._seperation_distance + 20))
                elif(self._board[row][col] != 0 and self._og_board[row][col] != 0):
                    if(self._once == False):
                        print(self._board[row][col])
                        self._once = True
                    text = self._font.render(str(self._board[row][col]), True, (0,0,255))
                    self._surface.blit(text, (col * self._seperation_distance + 34, row * self._seperation_distance + 20))
    



    def _create_surface(self, size: (int,int)) -> None:
        '''
        Create the Surface
        '''

        self._surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Sudoku Game")

    
    def _stop_running(self) -> None:
        self._running = False

    

    def _handle_events(self) -> None:
        '''
        Handles whether to quit or the resize the board
        '''
        for event in pygame.event.get():
            self._handle_event(event)

        self._handle_keys()


    def _handle_event(self, event) -> None:
        '''
        Handles whether to quit or the resize the board
        '''
        if event.type == pygame.QUIT:
            self._stop_running()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._handleMouseButton()


            
    def _handleMouseButton(self):
        self._mouseX, self._mouseY = pygame.mouse.get_pos()
        self._mouseX = self._mouseX // self._seperation_distance
        self._mouseY = self._mouseY // self._seperation_distance

        
        self._mouseClicked = True
        
       

    def _displayCurrentBox(self):
        pygame.draw.rect(self._surface, (135, 206, 250), (self._mouseX * self._seperation_distance + 2, self._mouseY * self._seperation_distance + 2, self._seperation_distance - 2 , self._seperation_distance - 2))


    def _handle_keys(self) -> None:
        '''
        Handles key presses to do an action
        '''

        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 1
                

        if keys[pygame.K_2]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 2

        if keys[pygame.K_3]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 3

        if keys[pygame.K_4]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 4
                
        if keys[pygame.K_5]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 5
        
        if keys[pygame.K_6]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 6

        if keys[pygame.K_7]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 7

        if keys[pygame.K_8]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 8

        if keys[pygame.K_9]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 9
        
        if keys[pygame.K_r]:
            self._reset_board(self._board, self._og_board)
        
        if keys[pygame.K_BACKSPACE]:
            if(self._og_board[int(self._mouseY)][int(self._mouseX)] == 0):
                self._board[int(self._mouseY)][int(self._mouseX)] = 0

        if keys[pygame.K_RETURN]:
            pass


        if self._check_filled():
            self._check_win()


if __name__ == '__main__':
    SudokuGrid().run()