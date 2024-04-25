"""Check Point Class."""

from __future__ import annotations


class Point():
    """Representation of x and y."""
    x: float 
    y: float 

    def __init__(self, x_init: float, y_init: float):
        """Defining constructor."""
        self.x = x_init
        self.y = y_init
        
    def scale_by(self, factor: int) -> None:
        """Mutates a point."""
        self.x = self.x * factor 
        self.y = self.y * factor 

    def scale(self, factor: int) -> Point:
        """Create new point."""
        return Point(self.x * factor, self.y * factor)
