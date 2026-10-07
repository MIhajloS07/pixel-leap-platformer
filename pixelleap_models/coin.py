from dataclasses import dataclass

@dataclass
class Coin:
    x: int                      # x position
    y: int                      # y position
    r: int                      # radius of circle
    value: int                  # coin value
    collected: bool = False     # storing bool value and using for checking if coin is collected (default -> False)