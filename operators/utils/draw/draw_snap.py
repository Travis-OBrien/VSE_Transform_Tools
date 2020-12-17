import bgl
from mathutils import Vector

from .draw_line import draw_line


def draw_snap(self, loc, orientation):
    """
    Draws the snap lines
    """
    color = (1.0, 1.0, 0.0, 0.5)
    outline_color = (0, 0, 0, 0.2)

    if orientation == "VERTICAL":
        v1 = [loc, -10000]
        v2 = [loc, 10000]

    elif orientation == "HORIZONTAL":
        v1 = [-10000, loc]
        v2 = [10000, loc]

    draw_line(v1, v2, 1.5, outline_color)   
    draw_line(v1, v2, 0.5, color)
