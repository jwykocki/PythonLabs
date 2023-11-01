# Napisz program, w którym dowolny tekst " Hello world! "
# przesuwa się w terminalu w pionie: w dół oraz w jakimś miejscu
# odbija się i do góry, aż do krawędzi okienka itd.

import time
import random

text = "Hello world!"
durationTime = 30
width = 50
length = 20
positionX = random.randrange(width)
positionY = random.randrange(length)
directionX = 1
directionY = -1
endTime = time.time() + durationTime

while time.time() < endTime:
    print("\n" * positionY, end='\r', flush=True)
    print('\r' + ' ' * positionX + text + ' ' * (width - positionX), end='', flush=True)
    print("\n" * (length - positionY), end='\r', flush=True)
    positionX += directionX
    positionY += directionY
    if positionX == width or positionX == 0:
        directionX *= -1
    if positionY == 0 or positionY == length:
        directionY *= -1

    time.sleep(0.2)
print()
