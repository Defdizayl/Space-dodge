import pygame
import time
import random
pygame.font.init()
WIDTH, HEIGHT = 900, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
BG = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("comicsans", 30)

STAR_WIDTH =10
STAR_HEIGHT =20
STAR_VEL = 3
PLAYER_WIDTH = 35
PLAYER_HEIGHT = 55
PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, pass_time, stars):
    WINDOW.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(pass_time)}s", 1, "yellow")
    WINDOW.blit(time_text, (800, 10))
    pygame.draw.rect(WINDOW, "white", player)
    for star in stars:
        pygame.draw.rect(WINDOW, "red", star)
    pygame.display.update()
    
def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    pass_time = 0
    star_add_increment = 2000
    star_count = 0
    stars = []
    hit = False
    
    while run:
        star_count += clock.tick(60)
        pass_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, - STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increment = max(200, star_add_increment - 50)
            star_count =0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >=0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <=WIDTH:
            player.x += PLAYER_VEL
        
        for star in stars[:]:
            star.y +=STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text = FONT.render("you lost!", 1, "white")
            WINDOW.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, pass_time, stars)
    pygame.quit()
    
if __name__== "__main__":
    main()

