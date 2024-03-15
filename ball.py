import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the ball properties
BALL_RADIUS = 20
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [5, 5]

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check for collision with the screen edges
    if ball_pos[0] - BALL_RADIUS <= 0 or ball_pos[0] + BALL_RADIUS >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)