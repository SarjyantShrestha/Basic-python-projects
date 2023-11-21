import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def generate_tiles(num):
    return set([
        (random.randrange(0, GRID_WIDTH), (random.randrange(0, GRID_HEIGHT))) for _ in range(num)
    ])


def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col*TILE_SIZE, row*TILE_SIZE)

        # if (10, 10) is tuple then rect(10, 10, 20, 20)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row*TILE_SIZE),
                         (WIDTH, row*TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col*TILE_SIZE, 0),
                         (col*TILE_SIZE, HEIGHT))


def main():
    running = True
    playing = False

    positions = set()
    positions.add((10, 10))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()

                if event.key == pygame.K_g:
                    positions = generate_tiles(
                        random.randrange(2, 10)*TILE_SIZE)

        screen.fill("grey")

        clock.tick(FPS)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()