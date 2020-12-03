import pygame
import random


class Snake:

    def __init__(self, display, colour, sw, sh):
        global direction
        self.x = 400
        self.y = 300
        self.dx = 0
        self.dy = 20
        self.jumps = 20
        self.positions = [(self.x, self.y)]
        self.food_eaten = 1
        self.food_x = 200
        self.food_y = 200
        self.sw = sw
        self.sh = sh
        self.screen = display
        self.colour = colour
        self.body = pygame.image.load("Images/snake.png")

    def draw_snake(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.body, (self.x, self.y))
        self.food()
        self.movement()
        self.tail()

    def movement(self):
        self.x += self.dx
        self.y += self.dy
        if direction == "w" and self.dy != self.jumps:
            self.dx = 0
            self.dy = -self.jumps

        if direction == "a" and self.dx != self.jumps:
            self.dx = -self.jumps
            self.dy = 0

        if direction == "s" and self.dy != -self.jumps:
            self.dx = 0
            self.dy = self.jumps

        if direction == "d" and self.dx != -self.jumps:
            self.dx = self.jumps
            self.dy = 0

        # stops snake from disappearing off the screen
        if self.x == 0:
            self.x = self.sw
        elif self.x == self.sw:
            self.x = 0
        elif self.y == 0:
            self.y = self.sh
        elif self.y == self.sh:
            self.y = 0

        self.positions.append((self.x, self.y))

    def tail(self):
        for i in range(1, self.food_eaten + 1):
            self.screen.blit(self.body, self.positions[-i - 1])

        # This is the maximum no. of squares pn the board. Start deleting
        # positions to keep list to a minimum size
        if len(self.positions) == 1200:
            del self.positions[0]

    def food(self):
        self.screen.blit(self.body, (self.food_x, self.food_y))
        if (self.x, self.y) == (self.food_x, self.food_y):
            self.food_eaten += 1
            self.food_x, self.food_y = 20 * random.randint(1, 39), \
                                       20 * random.randint(1, 29)


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

        snake.draw_snake()

        pygame.display.update()
        clock.tick(10)

    pygame.quit()
    quit()
