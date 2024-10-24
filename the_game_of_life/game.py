import pygame

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

def draw_grid(positions):
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE),(WIDTH, row * CELL_SIZE))
    for col in range (GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * CELL_SIZE, 0),(col* CELL_SIZE, HEIGHT))

def main():
    running = True
    positions = set()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()