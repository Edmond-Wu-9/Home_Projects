import pygame
import random

#Initialize PyGame
pygame.init()

# Declare Constants 
WIDTH, HEIGHT = 1000 , 1000 
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 60 

# Colors 
WHITE = (255, 255, 255) # Alive
BLACK = (0, 0, 0) # Base
GREY = (192,192,192)
RED = (255, 0, 0) # Dead

# Create a screen object
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Edmond's Game of Life")

# Create a clock 
clock  = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0,GRID_WIDTH)) for x in range(num)])

def draw_grid(positions):
    for position in positions:
        col,row = position
        top_left = (col * CELL_SIZE, row * CELL_SIZE)
        pygame.draw.rect(screen, RED, (*top_left, CELL_SIZE , CELL_SIZE))
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE),(WIDTH, row * CELL_SIZE))
    for col in range (GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * CELL_SIZE, 0),(col* CELL_SIZE, HEIGHT))

def main():
    running = True
    playing = False
    positions = set()
    positions.add((10,10))
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
                if (col, row) in positions:
                    positions.remove((col, row))
                else:
                    positions.add((col, row))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                if event.key == pygame.K_c:
                    positions.clear()
                    playing = False
                if event.key == pygame.K_g:
                    positions = gen(random.randrange(2,5) * GRID_WIDTH)
        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()