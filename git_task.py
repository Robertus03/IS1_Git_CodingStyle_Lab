import pygame
import random

# Inițializare Pygame
pygame.init()

# Constante
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
REGEN_INTERVAL = 5000  # 5 secunde în milisecunde

# Creare fereastră
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")


def generate_color_grid():
    """
    Generează o matrice GRID_SIZE x GRID_SIZE
    cu culori random (RGB).
    """
    return [
        [
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]


def draw_grid(grid):
    """
    Desenează grila pe ecran.
    """
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = grid[y][x]
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)


# Date inițiale
color_grid = generate_color_grid()
last_update_time = pygame.time.get_ticks()

running = True
while running:
    # Umple fundalul
    screen.fill((0, 0, 0))

    # Desenează grila
    draw_grid(color_grid)

    # Verifică timpul pentru regenerare automată (la 5 secunde)
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= REGEN_INTERVAL:
        color_grid = generate_color_grid()
        last_update_time = current_time

    # Evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Regenerare manuală la apăsarea SPACE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color_grid = generate_color_grid()
                last_update_time = pygame.time.get_ticks()

    # Actualizare ecran
    pygame.display.flip()

# Închidere Pygame
pygame.quit()