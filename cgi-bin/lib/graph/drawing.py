# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

from PIL import Image, ImageDraw, ImageFont
from .getaxes import get
from .. import const, web
from ..log import *
from ..driver.api import API

WIDTH = const.X_REAL_RESOLUTION * const.PIXELS_PER_MM   # 210 mm
HEIGHT = const.Y_REAL_RESOLUTION * const.PIXELS_PER_MM  # 297 mm
CENTER = HEIGHT // 2
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# drawing GIF image
def draw(points_iter, name, ptype, SCALE, settings, preview):

    font = ImageFont.truetype("Ubuntu-C.ttf", 20)
    log(preview)
    if preview:
        # PIL create an empty image and draw object to draw on
        # memory only, not visible
        image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        draw = ImageDraw.Draw(image)
    else:
        draw = API(const.CNC_PATH + name + const.CNC_EXT)


    if ptype is "graphic":
        draw.line([0, HEIGHT / 2, WIDTH, HEIGHT / 2], BLACK)
        draw.line([WIDTH / 2, 0, WIDTH / 2, HEIGHT], BLACK)
        
        step, koeff, k = get(WIDTH, SCALE)
        
        x = 1
        for i in range(step, (WIDTH // 2) * koeff, step):
            new = i / koeff
            draw.text((new + WIDTH / 2, (HEIGHT / 2) + 5), str(x / k), BLACK, font=font)
            draw.line(
                        [new + WIDTH / 2,
                       (HEIGHT / 2) - 5,
                       new + WIDTH / 2,
                       (HEIGHT / 2) + 5], BLACK)
            draw.text((-new + WIDTH / 2, (HEIGHT / 2) + 5), str(-x / k), BLACK, font=font)
            draw.line(
                        [-new + WIDTH / 2,
                       (HEIGHT / 2) - 5,
                       -new + WIDTH / 2,
                       (HEIGHT / 2) + 5], BLACK)
            x += 1
        
        y = 1
        for i in range(step, (HEIGHT // 2) * koeff, step):
            new = i / koeff
            draw.text((WIDTH / 2 + 5, (HEIGHT / 2) + new), str(-y / k), BLACK, font=font)
            draw.line(
                        [WIDTH / 2 - 5,
                       (HEIGHT / 2) + new,
                       WIDTH / 2 + 5,
                       (HEIGHT / 2) + new], BLACK)
            draw.text((WIDTH / 2 + 5, (HEIGHT / 2) - new), str(y / k), BLACK, font=font)
            draw.line(
                        [WIDTH / 2 - 5,
                       (HEIGHT / 2) - new,
                       WIDTH / 2 + 5,
                       (HEIGHT / 2) - new], BLACK)
            y += 1
    elif ptype is "bezier":
        p = SCALE
        if "draw_anchor" in settings and settings["draw_anchor"]:
            for i in p:
                draw.rectangle([i.x - 5, i.y + 5, i.x + 5, i.y - 5], outline=BLACK, fill="blue")
                
    if preview:
        last_point = None
        for pt in points_iter:
            # do the PIL image/draw (in memory) drawings
            if pt != None and last_point != None:
                draw.line([pt.x, pt.y,
                    last_point.x, last_point.y], RED)
            last_point = pt
    else:
        draw.draw_polylines(points_iter)


    if preview:
        web.update_status("Saving to file")
        # PIL image can be saved as .png .jpg .gif or .bmp file (among others)
        filename = const.IMAGE_PATH + name + const.IMAGE_EXT
        image.save(filename)
        web.update_status("Done")
    else:
        log("saving")
        draw.close()

