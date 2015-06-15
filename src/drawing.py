# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

from PIL import Image, ImageDraw

WIDTH = 1485
HEIGHT = 1050
CENTER = HEIGHT // 2
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SCALE = 100

# drawing GIF image
def draw(points, name, ptype):
    # PIL create an empty image and draw object to draw on
    # memory only, not visible
    image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)
    
    if ptype is "graphic":
        draw.line([0, HEIGHT / 2, WIDTH, HEIGHT / 2], BLACK)
        draw.line([WIDTH / 2, 0, WIDTH / 2, HEIGHT], BLACK)  
        
        nums = (WIDTH / 2)
        n = SCALE
        k = 1
        koeff = 1
        
        if nums // (SCALE / k) > 10:
            while nums // (SCALE / k) > 10:
                k /= 2
                koeff *= 2
                if nums // (SCALE / k) <= 10:
                    break
                k /= 5
                koeff *= 2
        else:
            while nums // (SCALE / k) < 10:
                k *= 2
                if nums // (SCALE / k) >= 10:
                    break      
                k *= 5
        
        step = SCALE / k
        count = nums // (SCALE / k)
        for i in range(int(step * koeff), (WIDTH // 2) * koeff, int(step * koeff)):
            new = i / koeff
            draw.line([new + WIDTH / 2,
                       (HEIGHT / 2) - 5,
                       new + WIDTH / 2,
                       (HEIGHT / 2) + 5], BLACK)
            draw.line([-new + WIDTH / 2,
                       (HEIGHT / 2) - 5,
                       -new + WIDTH / 2,
                       (HEIGHT / 2) + 5], BLACK) 
        
        for i in range(int(step * koeff), (HEIGHT // 2) * koeff, int(step * koeff)):
            new = i / koeff
            draw.line([WIDTH / 2 - 5,
                       (HEIGHT / 2) + new,
                       WIDTH / 2 + 5,
                       (HEIGHT / 2) + new], BLACK)
            draw.line([WIDTH / 2 - 5,
                       (HEIGHT / 2) - new,
                       WIDTH / 2 + 5,
                       (HEIGHT / 2) - new], BLACK)
                
                
    for i in range(len(points) - 1):
        # do the PIL image/draw (in memory) drawings
        draw.line([points[i].x, points[i].y,
                   points[i + 1].x, points[i + 1].y], RED)

    # PIL image can be saved as .png .jpg .gif or .bmp file (among others)
    filename = "../www/img/" + name + ".gif"
    image.save(filename)
    