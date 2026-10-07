from dataclasses import dataclass

@dataclass
class Enemy:
    x: int          # x coordinate
    y: int          # y coordinate
    w: int          # width
    h: int          # height
    vx: float       # speed for x coordinate
    min_x: float    # min x position
    max_x: float    # max x position
    color: tuple    # enemy color

