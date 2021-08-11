import pygame



_FRAME_RATE = 60


class SudokuGrid:

    def __init__(self):
        self._SCREEN_HEIGHT = 800
        self._SCREEN_WIDTH = 800
        self._running = True


    def run(self):
        pygame.init()

        try:
            clock = pygame.time.Clock()
            self._create_surface((self._SCREEN_WIDTH, self._SCREEN_HEIGHT))
            
            while self._running:
                clock.tick(_FRAME_RATE)
                self._handle_events()
                self._surface.fill((255,255,255))
                pygame.display.flip()


        
        finally:
            pygame.quit()



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