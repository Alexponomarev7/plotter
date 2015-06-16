# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.

from algorithmbezier import bezier, algorithmbezier
from drawing import draw


def main(name, p):
    print("Здравствуйте!")
    points = algorithmbezier(p)
    draw(points, name, "bezier", p)