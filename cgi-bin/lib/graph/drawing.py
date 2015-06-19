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

def draw_text(draw, pos, string, color, font):
    draw.text(pos, string, color, font=font)
    return ("t", (string, pos[0], pos[1]))

def draw_line(draw, coords, color):
    draw.line(coords, color)
    return ("l", ((coords[0], coords[1]), (coords[2], coords[3])))

def draw_rectangle(draw, coords, outline, fill):
    draw.rectangle(coords, outline=outline, fill=fill)
    return ("r", tuple(coords))

# drawing GIF image
def draw(points, name, ptype, SCALE = None, settings=None):
    font = ImageFont.truetype("Ubuntu-C.ttf", 20)
    # PIL create an empty image and draw object to draw on
    # memory only, not visible
    image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)

    aux_task = []
    
    if ptype is "graphic":
        aux_task.append(draw_line(draw, [0, HEIGHT / 2, WIDTH, HEIGHT / 2], BLACK))
        aux_task.append(draw_line(draw, [WIDTH / 2, 0, WIDTH / 2, HEIGHT], BLACK))
        
        step, koeff, k = get(WIDTH, SCALE)
        
        x = 1
        for i in range(step, (WIDTH // 2) * koeff, step):
            new = i / koeff
            aux_task.append(draw_text(draw, (new + WIDTH / 2, (HEIGHT / 2) + 5), str(x / k), BLACK, font))
            aux_task.append(
                    draw_line(draw, 
                        [new + WIDTH / 2,
                       (HEIGHT / 2) - 5,
                       new + WIDTH / 2,
                       (HEIGHT / 2) + 5], BLACK))
            aux_task.append(draw_text(draw, (-new + WIDTH / 2, (HEIGHT / 2) + 5), str(-x / k), BLACK, font))
            aux_task.append(
                    draw_line(draw, 
                        [-new + WIDTH / 2,
                       (HEIGHT / 2) - 5,
                       -new + WIDTH / 2,
                       (HEIGHT / 2) + 5], BLACK))
            x += 1
        
        y = 1
        for i in range(step, (HEIGHT // 2) * koeff, step):
            new = i / koeff
            aux_task.append(draw_text(draw, (WIDTH / 2 + 5, (HEIGHT / 2) + new), str(-y / k), BLACK, font))
            aux_task.append(
                    draw_line(draw, 
                        [WIDTH / 2 - 5,
                       (HEIGHT / 2) + new,
                       WIDTH / 2 + 5,
                       (HEIGHT / 2) + new], BLACK))
            aux_task.append(draw_text(draw, (WIDTH / 2 + 5, (HEIGHT / 2) - new), str(y / k), BLACK, font))
            aux_task.append(
                    draw_line(draw, 
                        [WIDTH / 2 - 5,
                       (HEIGHT / 2) - new,
                       WIDTH / 2 + 5,
                       (HEIGHT / 2) - new], BLACK))
            y += 1
    elif ptype is "bezier":
        p = SCALE
        if "draw_anchor" in settings and settings["draw_anchor"]:
            for i in p:
                aux_task.append(draw_rectangle(draw, [i.x - 5, i.y + 5, i.x + 5, i.y - 5], BLACK, "blue"))
                
    for i in range(len(points) - 1):
        # do the PIL image/draw (in memory) drawings
        if points[i] != None and points[i + 1] != None:
            draw.line([points[i].x, points[i].y,
                points[i + 1].x, points[i + 1].y], RED)

    # PIL image can be saved as .png .jpg .gif or .bmp file (among others)
    filename = const.IMAGE_PATH + name + ".gif"
    image.save(filename)
    return aux_task

