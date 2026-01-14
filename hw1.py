import pygame
pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BACKGROUND_COLOR = (255, 255, 255)
RECT_COLOR = (0, 100, 200)
TEXT_COLOR = (0, 0, 0) 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("my first game screen")
rectangle = pygame.Rect(0, 0, 50, 50)
rectangle.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
font = pygame.font.Font(None, 36)
text_surface = font.render("hello!", True, TEXT_COLOR)
text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, RECT_COLOR, rectangle)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
pygame.quit()
