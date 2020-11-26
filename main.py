import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake.. Snake!? SNAAAKKKEEE!!!!")

# colors
white = (255, 255, 255)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        print(event)

    pygame.draw.rect(screen, white, [400, 300, 10, 10])
    pygame.display.update()

pygame.quit()
quit()
