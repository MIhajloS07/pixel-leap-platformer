from dataclasses import dataclass

@dataclass
class MovingPlatform:
    x: int          # x coordinate
    y: int          # y coordinate
    w: int          # width
    h: int          # height
    vx: float       # speed for x coordinate
    vy: float       # speed for y coordinate
    min_x: float    # min x position
    max_x: float    # max x position
    min_y: float    # min y position
    max_y: float    # max y position