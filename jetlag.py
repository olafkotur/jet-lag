import sys, pygame

# Setup
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512
FPS = 30

# Colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

# Draw game
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

def main():
    drawPlayer()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        pygame.display.update()
        CLOCK.tick(30)
        


def drawPlayer():
    pygame.draw.circle(SCREEN, WHITE, [100, 100], 100, 50)

if __name__ == "__main__":
    main()