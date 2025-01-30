import pygame  

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = SCREEN_HEIGHT - 70

#create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("T-REX GAME")

clock = pygame.time.Clock()

#load assets
T_REX_WIDTH = 40
T_REX_HEIGHT = 50
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 50
t_rex_y = GROUND_HEIGHT - T_REX_HEIGHT

#jumping variables
is_jumping = False
jump_height = 12
jump_velocity = jump_height
gravity = 1

obstacle_x = SCREEN_WIDTH
obstacle_speed = 10

score = 0
font = pygame.font.Font(None, 36)

game_over = False

def check_collision(t_rex_rect, obstacle_rect):
    return t_rex_rect.colliderect(obstacle_rect)

#GAME LOOP
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #jumping
    keys = pygame.key.get_pressed()
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True

    if is_jumping:
        t_rex_y -= jump_velocity
        jump_velocity -= gravity

        if jump_velocity < -jump_height:
            is_jumping = False
            jump_velocity = jump_height

    if score % 5 == 0 and score > 0:
        obstacle_speed = 10 + (score // 5)

    t_rex_rect = pygame.Rect(50, t_rex_y, T_REX_WIDTH, T_REX_HEIGHT)
    pygame.draw.rect(screen, BLACK, t_rex_rect)

    obstacle_x -= obstacle_speed
    if obstacle_x < -OBSTACLE_WIDTH:
        obstacle_x = SCREEN_WIDTH
        score += 1
    
    obstacle_rect = pygame.Rect(obstacle_x, GROUND_HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    pygame.draw.rect(screen, BLACK, obstacle_rect)

    if check_collision(t_rex_rect, obstacle_rect):
        game_over = True
        break

    pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (SCREEN_WIDTH, GROUND_HEIGHT), 3)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

while game_over:
    screen.fill(WHITE)
    game_over_text = font.render("GAME OVER", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.quit:
            game_over = False

pygame.quit()