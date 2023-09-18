import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BMI Calculator")

# Variables
height = ""
weight = ""
bmi = 0

def calculate_bmi(height, weight):
    try:
        height_m = float(height) / 100
        weight_kg = float(weight)
        bmi = round(weight_kg / (height_m ** 2), 2)
        return bmi
    except ValueError:
        return None

def main():
    global height, weight, bmi

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    bmi = calculate_bmi(height, weight)
                elif event.key == pygame.K_BACKSPACE:
                    if len(height) > 0 or len(weight) > 0:
                        height = height[:-1]
                        weight = weight[:-1]
                else:
                    if event.unicode.isnumeric() or (event.unicode == '.' and '.' not in height):
                        if len(height) < 3:
                            height += event.unicode
                        elif len(weight) < 3:
                            weight += event.unicode

        # Clear the screen
        screen.fill(WHITE)

        # Display the input fields and result
        text_height = FONT.render(f"Height (cm): {height}", True, BLACK)
        text_weight = FONT.render(f"Weight (kg): {weight}", True, BLACK)
        text_bmi = FONT.render(f"BMI: {bmi}", True, BLACK)

        screen.blit(text_height, (50, 50))
        screen.blit(text_weight, (50, 100))
        screen.blit(text_bmi, (50, 200))

        pygame.display.flip()

if __name__ == "__main__":
    main()
