import pygame
import sys

def main():
    clock = pygame.time.Clock()
    pygame.init()

    pygame.display.set_caption('Moonball')

    pygame.mixer.music.load(r'music\once-in-paris.mp3')
    pygame.mixer.music.play(-1)

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    speed = [0, 0]
    accel = [0.5, 0.5]
    t = 1
    image = pygame.image.load(r'images\moon.jpg')
    image = pygame.transform.scale(image, size)

    surf_center = (
        (width - image.get_width()) / 2,
        (height - image.get_height()) / 2
    )

    font = pygame.font.Font(None, 36)  # Utwórz obiekt czcionki

    ball = pygame.image.load(r'images\ball.gif')
    ball = pygame.transform.scale(ball, (ball.get_width() // 2, ball.get_height() // 2))

    ballrect = ball.get_rect(center=(width / 2, height / 2))
    pygame.display.flip()

    while True:
        clock.tick(60)
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        if keys[pygame.K_UP]:
            speed[1] -= accel[1]*t  # Przyspieszanie do góry
        elif keys[pygame.K_DOWN]:
            speed[1] += accel[1]*t  # Przyspieszanie w dół
        elif keys[pygame.K_LEFT]:
            speed[0] -= accel[0]*t  # Przyspieszanie w lewo
        elif keys[pygame.K_RIGHT]:
            speed[0] += accel[0]*t  # Przyspieszanie w prawo

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)

        # Formatowanie i rysowanie informacji o prędkości i przyspieszeniu
        accel_text = font.render(f'Acceleration: ({accel[0]:.2f}, {accel[1]:.2f})', True, (255, 255, 255))
        speed_text = font.render(f'Speed: ({speed[0]:.2f}, {speed[1]:.2f})', True, (255, 255, 255))
        screen.blit(accel_text, (10, 10))
        screen.blit(speed_text, (10, 50))

        pygame.display.flip()

if __name__ == "__main__":
    main()
