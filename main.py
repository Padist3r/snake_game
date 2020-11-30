import pygame


class Snake:

    def __init__(self, display, colour, sw, sh):
        self.x = 400
        self.y = 300
        self.dx = 0
        self.dy = 10
        self.direction = None
        self.sw = sw
        self.sh = sh
        self.screen = display
        self.colour = colour
        self.body = pygame.image.load("Images/snake.png")

    def draw_snake(self, dxdy):
        self.direction = dxdy
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.body, (self.x, self.y))
        self.movement()

    def movement(self):
        self.x += self.dx
        self.y += self.dy
        if self.direction == "w":
            self.dx = 0
            self.dy = -10
        if self.direction == "a":
            self.dx = -10
            self.dy = 0
        if self.direction == "s":
            self.dx = 0
            self.dy = 10
        if self.direction == "d":
            self.dx = 10
            self.dy = 0

    def tail(self):
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
    direction = None

    # clock
    clock = pygame.time.Clock()

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == ord("w"):
                    direction = "w"
                elif event.key == ord("a"):
                    direction = "a"
                elif event.key == ord("s"):
                    direction = "s"
                elif event.key == ord("d"):
                    direction = "d"

        snake.draw_snake(direction)

        pygame.display.update()
        clock.tick(5)

    pygame.quit()
    quit()
