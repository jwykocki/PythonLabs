# Najpierw należy przestudiować załączony kod (main.py wszystko w jednym pliku), jest to klasyczna gra
# w ping-ponga, napisana z użyciem znanej nam biblioteki pygame. Proszę po kolei przestudiować kod, który
# jest komentowany i choć (ewentualnie) zawiera rzeczy nowe, to można się domyślić o co chodzi. W szczególności
# na początku są definicje dwóch klas Rakietka i Pilka, które zapisane są jako dziedziczące z klasy pygame.sprite.Sprite
# (proszę zobaczyć w kodzie jak to wygląda). Klasy są dość proste, ich metody dbają o zmianę i sprawdzenie położeń
# granicznych oraz ustalanie (np. losowanie w pewnym zakresie) wartości prędkości piłki. Program zaczyna się od
# narysowania ekranu, rakietek, piłki (piłka jest o rozmiarze 10x10 punktów), utworzeniu listy widzialnych w grze
# obiektów (właśnie odziedziczonych z klasy Sprite). Sama mechanika ruchów rakietek powinna być już znana z poprzednich
# zadań, ciekawa jest metoda collide_mask sprawdzająca czy dane dwa obiekty nie są ze sobą w styczności / kolizji, jeśli
# tak jest, to na rzecz piłeczki wołamy metodę bounce(), która zmienia (i trochę losuje) składową prędkości piłki po odbiciu.
# Zadanie: po przestudiowaniu i uruchomieniu kodu zadanie będzie polegać na takim jego zmodyfikowaniu, żeby: (a) rakietka była
# tylko jedna, poruszająca się w poziomie na dole ekranu (w lewo i prawo, strzałkami), (b) piłeczka uruchamiana losowo z góry,
# punkty mają być naliczane za poprawne odbicie od rakietki, (c) gra ma się zakończyć jeśli piłeczka minie rakietkę i zderzy się
# ze ścianą – wtedy powinien się wyświetlić wynik końcowy oraz dotychczasowy najwyższy wynik. Najlepszy wynik zapisywać do i
# odczytywać z pliku. Oczywiście pionowa linia jest teraz zbędna. Innymi słowy – przerobić to na grę „jednoosobową”
# [zadanie za 2 pkt].

import pygame
from random import randint
import json

# Otwieranie pliku JSON i odczytywanie danych
with open("game_data.json", "r") as json_file:
    data = json.load(json_file)
    best_score = data.get("best_score", None)

# Sprawdzenie, czy zmienna best_score została odczytana
if best_score is None:
    best_score = 0

pygame.init()
# kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Paddle(pygame.sprite.Sprite):

    # klasa Paddle dziedziczy z klasy "Sprite" w Pygame.
    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x <= 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x >= 600:
           self.rect.x = 600



class Ball(pygame.sprite.Sprite):

    # klasa Ball dziedziczy ze "Sprite" w Pygame.
    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(-8, 8), randint(4, 6)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = randint(-8,8)



# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 480

ball = Ball(WHITE, 10, 10)
ball.rect.x = 200
ball.rect.y = 10

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie obu rakietek i piłeczki do listy
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

# zaczynamy właściwy blok programu
continue_game = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowe wyniki graczy
user_score = 0

# -------- GLÓWNA PĘTLA PROGRAMU -----------

pygame.time.delay(2000)
while continue_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            continue_game = False

    # ruchy obiektów Rakietkas klawisze strzałki
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)


    # aktualizacja listy duszków
    all_sprites_list.update()

    # sprawdzenie czy piłeczka nie uderza w którąś ścianę
    # i odpowiednie naliczenie punktu jeśli minie rakietkę A lub B i uderzy w ścianę za nią
    # if pileczka.rect.y<=20:
    #     scoreA+=1
    #     pileczka.velocity[1] = -pileczka.velocity[1]
    if ball.rect.y>=490:
        continue_game = False
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=10:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    # sprawdzenie kolizji piłeczki z obiektem rakietkaA lub rakietkaB
    if pygame.sprite.collide_mask(ball, paddle):
      ball.bounce()
      user_score += 1

    # RYSOWANIE
    # czarny ekran
    screen.fill(BLACK)

    # narysowanie obiektów
    all_sprites_list.draw(screen)

    # wyświetlanie wyników
    font = pygame.font.Font(None, 30)
    text = font.render("Your score: " + str(user_score), 1, WHITE)
    text2 = font.render("Best score: " + str(best_score), 1, WHITE)
    screen.blit(text, (50,10))
    screen.blit(text2, (50, 40))

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec

screen.fill(BLACK)
font = pygame.font.Font(None, 30)

if(best_score is None or user_score > best_score):
    data_to_save = {"best_score": user_score}
    text5 = font.render("Your score is new best score!", 1, WHITE)
    with open("game_data.json", "w") as json_file:
        json.dump(data_to_save, json_file)
else:
    text5 = font.render("Nice try!", 1, WHITE)
text3 = font.render("Your score: " + str(user_score), 1, WHITE)
text4 = font.render("Best score: " + str(best_score), 1, WHITE)
text6 = font.render("Press any key to exit", 1, WHITE)
screen.blit(text3, (200,110))
screen.blit(text4, (200, 140))
screen.blit(text5, (200, 170))
screen.blit(text6, (200, 200))
pygame.display.flip()

# czekanie na naciśnięcie dowolnego klawisza
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            waiting = False

pygame.quit()
