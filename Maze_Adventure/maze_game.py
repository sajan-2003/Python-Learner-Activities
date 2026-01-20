import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Adventure")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
GREEN = (50, 200, 100)
GRAY = (100, 100, 100)

# Clock
clock = pygame.time.Clock()

# Player
player = pygame.Rect(50, 50, 40, 40)
player_speed = 5

# Goal
goal = pygame.Rect(700, 500, 50, 50)

# Walls
walls = [
    pygame.Rect(200, 0, 40, 400),
    pygame.Rect(400, 200, 40, 400),
    pygame.Rect(600, 0, 40, 400),
]

def move_player(keys):
    dx, dy = 0, 0
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        dy -= player_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dy += player_speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx += player_speed

    player.x += dx
    for wall in walls:
        if player.colliderect(wall):
            player.x -= dx

    player.y += dy
    for wall in walls:
        if player.colliderect(wall):
            player.y -= dy

# Main game loop
running = True
win = False

while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not win:
        move_player(keys)

    # Draw elements
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, GREEN, goal)
    for wall in walls:
        pygame.draw.rect(screen, GRAY, wall)

    # Win condition
    if player.colliderect(goal):
        win = True
        font = pygame.font.SysFont(None, 64)
        text = font.render("YOU WIN!", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()
