import pygame
import random


class Snake:

    def __init__(self, display, colour, sw, sh):
        global direction
        self.height, self.width = 20, 20
        self.x = 400
        self.y = 300
        self.dx = 0
        self.dy = 20
        self.jumps = 20
        self.positions = [(self.x, self.y)]
        self.snake_alive = True
        self.food_eaten = 1
        self.food_x = 200
        self.food_y = 200
        self.sw = sw
        self.sh = sh
        self.screen = display
        self.colour = colour

    def draw_snake(self):
        pygame.draw.rect(self.screen, self.colour,
                         (self.x, self.y, self.height, self.width))
        self.food()
        self.movement()
        self.tail()

    def movement(self):
        self.x += self.dx
        self.y += self.dy

        # this code lets you control snake and also stops him from turning
        # back on himself
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
        if self.x < 20:
            self.x = self.sw - 40
        elif self.x > self.sw - 40:
            self.x = 20
        elif self.y < 20:
            self.y = self.sh - 40
        elif self.y > self.sh - 40:
            self.y = 20

        if self.snake_alive:
            self.positions.append((self.x, self.y))

    def tail(self):
        for i in range(1, self.food_eaten + 1):
            pygame.draw.rect(self.screen, self.colour,
                             (self.positions[-i - 1][0],
                              self.positions[-i - 1][1],
                              self.height, self.width))
            # if snake hits his tail, stop him moving as game is over
            if self.positions[-i - 1] == (self.x, self.y):
                self.snake_alive = False
                self.dx = 0
                self.dy = 0

        # This is the maximum no. of squares pn the board. Start deleting
        # positions to keep list to a relatively low size.
        # can probably make this more memory efficient but space is not an
        # issue at the minute
        if len(self.positions) == 1200:
            del self.positions[0]

    def food(self):
        pygame.draw.rect(self.screen, self.colour,
                         (self.food_x, self.food_y, self.height, self.width))
        if (self.x, self.y) == (self.food_x, self.food_y):
            self.food_eaten += 1
            self.food_x, self.food_y = 20 * random.randint(1, 38), \
                                       20 * random.randint(1, 28)


def main_screen():
    pygame.draw.line(screen, white, (20, 20), (780, 20))
    pygame.draw.line(screen, white, (20, 580), (780, 580))
    pygame.draw.line(screen, white, (20, 20), (20, 580))
    pygame.draw.line(screen, white, (780, 20), (780, 580))
    # text
    font = pygame.font.Font("freesansbold.ttf", 20)
    score_text = font.render(f"Score: {snake.food_eaten - 1}", True, white,
                             black)
    score_rect = score_text.get_rect()
    score_rect.center = (60, 10)
    screen.blit(score_text, score_rect)


def game_over_screen():
    pygame.draw.line(screen, white, (20, 20), (780, 20))
    pygame.draw.line(screen, white, (20, 580), (780, 580))
    pygame.draw.line(screen, white, (20, 20), (20, 580))
    pygame.draw.line(screen, white, (780, 20), (780, 580))
    # text
    font = pygame.font.Font("freesansbold.ttf", 60)
    game_over_text = font.render("Game Over!", True, white,
                             black)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (400, 300)
    screen.blit(game_over_text, game_over_rect)


if __name__ == '__main__':

    pygame.init()

    # display
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake.. Snake!? SNAAAKKKEEE!!!!")

    # colors
    white = (255, 255, 255)
    black = (0, 0, 0)

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

        screen.fill((0, 0, 0))
        if snake.snake_alive:
            snake.draw_snake()
            main_screen()
        else:
            game_over_screen()

        pygame.display.update()
        clock.tick(15)

    pygame.quit()
    quit()
