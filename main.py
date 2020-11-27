import pygame


class Snake:

    def __init__(self, display, colour, sw, sh):
        self.x = 400
        self.y = 300
        self.dx = 0
        self.dy = 10
        self.dir = ""
        self.size = 10
        self.sw = sw
        self.sh = sh
        self.screen = display
        self.colour = colour
        self.body = pygame.image.load("Images/snake.png")

    def draw_snake(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.body, (self.x, self.y))
        self.movement()

    def movement(self):
        pass


if __name__ == '__main__':

    pygame.init()

    # display
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake.. Snake!? SNAAAKKKEEE!!!!")

    # colors
    white = (255, 255, 255)

    # snake
    snake = Snake(screen, white, width, height)

    # clock
    clock = pygame.time.Clock()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            print(event)

        snake.draw_snake()

        pygame.display.update()
        clock.tick(10)

    pygame.quit()
    quit()
