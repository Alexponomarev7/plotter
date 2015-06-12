# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

from PIL import Image, ImageDraw

WIDTH = 500
HEIGHT = 500
CENTER = HEIGHT // 2
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#drawing GIF image
def draw(points, name):
    # PIL create an empty image and draw object to draw on
    # memory only, not visible
    image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)
    
    for i in range(len(points) - 1):
        # do the PIL image/draw (in memory) drawings
        draw.line([points[i].x + WIDTH // 2,
                   points[i].y + HEIGHT // 2,
                   points[i + 1].x + WIDTH // 2,
                   points[i + 1].y + HEIGHT // 2], RED)

    # PIL image can be saved as .png .jpg .gif or .bmp file (among others)
    filename = name + ".gif"
    image.save(filename)
    
    
    
    
