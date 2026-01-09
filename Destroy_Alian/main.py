# main.py
import pygame
from Src.Guns import Player

# Initialize pygame
pygame.init()
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Destroy Alian - Player Test")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create player object
player = Player(x=screen_width//2, y=screen_height-50, screen_width=screen_width)

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_SPACE]:
        player.shoot()

    # Update bullets
    player.update_bullets(screen_height)

    # Draw player (rectangle)
    pygame.draw.rect(screen, WHITE, (player.x-15, player.y-15, 30, 30))

    # Draw bullets
    for bullet in player.bullets:
        pygame.draw.rect(screen, WHITE, (bullet.x-5, bullet.y-10, 10, 20))

    # Update display
    pygame.display.flip()

pygame.quit()
