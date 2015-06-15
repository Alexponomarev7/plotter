from tkinter import *
from point import point 
from algorithmbezier import bezier, algorithmbezier
from drawing import draw


def main(name, p):
    print("Здравствуйте!")
    # root = Tk()
    # panel = Canvas(root, width = 500, height = 500)
    # panel.pack()
    
    # nums = [int(x) for x in input().split()]
    # p = []
    # p = [point(10, 60), point(200, 20), point(90, 200), point(400, 500)]
    # p = [point(200, 100), point(400, 400), point(100, 400), point(300, 100)]
    # p = [point(100, 100), point(400, 100), point(400, 400), point(100, 400), point(100, 100)]
    # for i in range(0, len(nums), 2):
    #    p.append(point(nums[i], nums[i + 1]))
    
    points = algorithmbezier(p)
    
    # for i in range(len(points) - 1):
    #    panel.create_line(points[i].x, points[i].y, points[i + 1].x, points[i + 1].y, fill="red")
    draw(points, name, "bezier")
    
    # root.mainloop()
    
