import pygame



_FRAME_RATE = 10


class SudokuGrid:
    board = [
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

    def __init__(self):
        self._SCREEN_HEIGHT = 800
        self._SCREEN_WIDTH = 800
        self._running = True
        self._seperation_distance = self._SCREEN_WIDTH / 9
        


    def run(self):
        pygame.init()

        try:
            clock = pygame.time.Clock()
            self._create_surface((self._SCREEN_WIDTH, self._SCREEN_HEIGHT))
            
            while self._running:

                clock.tick(_FRAME_RATE)

                self._handle_events()

                self._surface.fill((255,255,255))
                self._draw_lines()
                pygame.display.flip()


        
        finally:
            pygame.quit()


    def _draw_lines(self):
        for i in range(10):
            if(i % 3 == 0):
                pygame.draw.line(self._surface, (0, 0, 0), (0, i*self._seperation_distance), (self._SCREEN_WIDTH, i * self._seperation_distance), 8)
                pygame.draw.line(self._surface, (0, 0, 0), (i * self._seperation_distance, 0), (i * self._seperation_distance, self._SCREEN_HEIGHT), 8)
            else:
                pygame.draw.line(self._surface, (0, 0, 0), (0, i*self._seperation_distance), (self._SCREEN_WIDTH, i * self._seperation_distance), 3)
                pygame.draw.line(self._surface, (0, 0, 0), (i * self._seperation_distance, 0), (i * self._seperation_distance, self._SCREEN_HEIGHT), 3)
            





    def _create_surface(self, size: (int,int)) -> None:
        '''
        Create the Resizable Surface
        '''

        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption("Sudoku Game")

    
    def _stop_running(self) -> None:
        self._running = False

    

    def _handle_events(self) -> None:
        '''
        Handles whether to quit or the resize the board
        '''
        for event in pygame.event.get():
            self._handle_event(event)

        # self._handle_keys()


    def _handle_event(self, event) -> None:
        '''
        Handles whether to quit or the resize the board
        '''
        if event.type == pygame.QUIT:
            self._stop_running()

        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, flags=pygame.RESIZABLE)
            self._SCREEN_WIDTH = event.size[0]
            self._SCREEN_HEIGHT = event.size[1]
            self._seperation_distance = self._SCREEN_WIDTH / 9

            
    # def _handle_keys(self) -> None:
    #     '''
    #     Handles key presses to do an action
    #     '''

    #     keys = pygame.key.get_pressed()

    #     if keys[pygame.K_LEFT]:
    #         self._board.check_left()

    #     if keys[pygame.K_RIGHT]:
    #         self._board.check_right()

    #     if keys[pygame.K_SPACE]:
    #         self._board.rotate()




if __name__ == '__main__':
    SudokuGrid().run()