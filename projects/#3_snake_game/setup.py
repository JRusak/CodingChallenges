import pygame
from snake import Snake
from food import Food

YELLOW = (255, 255, 0)


def setup(width, height, cell_size, top_offset):
    pygame.init()
    pygame.display.set_mode([width, height])
    pygame.display.set_caption('Snake')
    font_style = pygame.font.Font(None, 50)

    s = Snake(cell_size, top_offset)
    f = Food(s, cell_size, top_offset)

    return s, f, font_style


def draw(snake, snake_speed, food, font_style):
    width = pygame.display.get_window_size()[0]
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_pressed(snake, event)
                break

        screen.fill((51, 51, 51))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, 50))

        snake.update(food)
        snake.show()
        food.show()

        message(f'Score: {snake.total - 1}', YELLOW, screen, font_style)

        pygame.display.flip()

        clock.tick(snake_speed)


def message(msg, color, display, font_style):
    m = font_style.render(msg, True, color)
    display.blit(m, [10, 10])


def key_pressed(snake, event):
    if event.key == pygame.K_UP:
        snake.dir('UP')
    elif event.key == pygame.K_DOWN:
        snake.dir('DOWN')
    elif event.key == pygame.K_LEFT:
        snake.dir('LEFT')
    elif event.key == pygame.K_RIGHT:
        snake.dir('RIGHT')


def main():
    width = 600
    height = 650

    snake_speed = 5

    top_offset = 50
    cell_size = 60

    snake, food, font_style = setup(width, height, cell_size, top_offset)
    draw(snake, snake_speed, food, font_style)


if __name__ == '__main__':
    main()
