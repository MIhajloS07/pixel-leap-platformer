from dataclasses import dataclass
from pygame.math import Vector2

@dataclass
class Player:
    p: Vector2       # position
    v: Vector2       # speed
    w: int           # width
    h: int           # height
    on_base: bool    # if player is on something (some object)
    is_jumping: bool # if player jumping -> True, otherwise False
    lives: int       # number of lives