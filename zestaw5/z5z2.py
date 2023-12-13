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

    speed = [10, 10]  # Prędkość początkowa piłki (vx, vy)
    accel = [0, 9.81]  # Przyspieszenie grawitacyjne (ax, ay)
    t = 0.2

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

        # Aktualizacja prędkości na podstawie przyspieszenia
        speed[0] += accel[0] * t
        speed[1] += accel[1] * t

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)

        # Rysowanie informacji o prędkości
        speed_text = font.render(f'Speed: ({speed[0]:.2f}, {speed[1]:.2f})', True, (255, 255, 255))
        screen.blit(speed_text, (10, 50))

        pygame.display.flip()

if __name__ == "__main__":
    main()
