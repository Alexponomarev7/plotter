# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

from PIL import Image, ImageDraw, ImageFont
from .getaxes import get
from .. import const

WIDTH = const.X_REAL_RESOLUTION * const.PIXELS_PER_MM   # 210 mm
HEIGHT = const.Y_REAL_RESOLUTION * const.PIXELS_PER_MM  # 297 mm
CENTER = HEIGHT // 2
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# drawing GIF image
def draw(points, name, ptype, SCALE = None):
    font = ImageFont.truetype(font="Arial", size=20)
    # PIL create an empty image and draw object to draw on
    # memory only, not visible
    image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)
    
    if ptype is "graphic":
        draw.line([0, HEIGHT / 2, WIDTH, HEIGHT / 2], BLACK)
        draw.line([WIDTH / 2, 0, WIDTH / 2, HEIGHT], BLACK)  
        
        step, koeff, k = get(WIDTH, SCALE)
        
        x = 1
        for i in range(step, (WIDTH // 2) * koeff, step):
            new = i / koeff
            draw.text((new + WIDTH / 2, (HEIGHT / 2) + 5), str(x / k), BLACK, font=font)
            draw.line([new + WIDTH / 2,
                       (HEIGHT / 2) - 5,
                       new + WIDTH / 2,
                       (HEIGHT / 2) + 5], BLACK)
            draw.text((-new + WIDTH / 2, (HEIGHT / 2) + 5), str(-x / k), BLACK, font=font)            
            draw.line([-new + WIDTH / 2,
                       (HEIGHT / 2) - 5,
                       -new + WIDTH / 2,
                       (HEIGHT / 2) + 5], BLACK)
            x += 1
        
        y = 1
        for i in range(step, (HEIGHT // 2) * koeff, step):
            new = i / koeff
            draw.text((WIDTH / 2 + 5, (HEIGHT / 2) + new), str(-y / k), BLACK, font=font)            
            draw.line([WIDTH / 2 - 5,
                       (HEIGHT / 2) + new,
                       WIDTH / 2 + 5,
                       (HEIGHT / 2) + new], BLACK)
            draw.text((WIDTH / 2 + 5, (HEIGHT / 2) - new), str(y / k), BLACK, font=font)                        
            draw.line([WIDTH / 2 - 5,
                       (HEIGHT / 2) - new,
                       WIDTH / 2 + 5,
                       (HEIGHT / 2) - new], BLACK)
            y += 1
    elif ptype is "bezier":
        p = SCALE
        for i in p:
            draw.rectangle([i.x - 5, i.y + 5, i.x + 5, i.y - 5], outline=BLACK, fill="blue")
                
    for i in range(len(points) - 1):
        # do the PIL image/draw (in memory) drawings
        if points[i] != None and points[i + 1] != None:
            draw.line([points[i].x, points[i].y,
                points[i + 1].x, points[i + 1].y], RED)

    # PIL image can be saved as .png .jpg .gif or .bmp file (among others)
    filename = const.IMAGE_PATH + name + ".gif"
    image.save(filename)
    
