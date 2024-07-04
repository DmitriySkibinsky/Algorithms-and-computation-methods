import pygame
from sys import exit

# Background color, lines between points, and curve color.
BLACK = (0, 0, 0)
WHITE = (100, 100, 100)
RED = (58, 243, 53)
dots = []  # List for control points
curve = []  # List of curve points
press = 0  # Variable acting as a flag
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:  # Event to reset all data on TAB key press
                dots = []
                curve = []
                press = 0
        if event.type == pygame.MOUSEBUTTONDOWN:  # Handling left mouse button press
            if event.button == 1:
                if press == 0:  # Case when the flag is zero
                    press = 1
                    dots = [event.pos, event.pos, event.pos,
                            event.pos]  # Adding 4 points with the position values of the click
                elif press == 1:
                    press = 2
                elif press == 2:
                    press = 3
                elif press == 3:
                    press = -1
        # Handling mouse movement event on the screen. Depending on the flag value, the corresponding point is updated.
        if event.type == pygame.MOUSEMOTION:
            if press == 1:
                dots[3] = event.pos
            elif press == 2:
                dots[2] = event.pos
            elif press == 3:
                dots[1] = event.pos

    screen.fill(BLACK)
    if dots:
        pygame.draw.aalines(screen, WHITE, False, dots)  # Drawing lines between points
        for dot in dots:
            pygame.draw.circle(screen, WHITE, dot, 5, 1)  # Adding circles to highlight control points
        curve = []  # Clearing the list of curve points to dynamically draw it every frame
        for i in map(lambda x: x / 100.0, range(0, 105,
                                                5)):  # Using map with lambda function to generate a list of fractional values for t
            x = (1.0 - i) ** 3 * dots[0][0] + 3 * (1.0 - i) ** 2 * i * dots[1][0] + 3 * (1.0 - i) * i ** 2 * dots[2][
                0] + i ** 3 * dots[3][0]  # Cubic Bezier curve formula for X and Y values
            y = (1.0 - i) ** 3 * dots[0][1] + 3 * (1.0 - i) ** 2 * i * dots[1][1] + 3 * (1.0 - i) * i ** 2 * dots[2][
                1] + i ** 3 * dots[3][1]
            curve.append([x, y])
        pygame.draw.lines(screen, RED, False, curve, 3)  # Drawing the curve

    pygame.display.flip()
    clock.tick(30)
