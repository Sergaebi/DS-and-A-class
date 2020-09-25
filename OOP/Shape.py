import abc
import math


class Shape(abc.ABC):

    def __init__(self, color="red", filled=True):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        self._color = new_color

    color = property(get_color, set_color)
        
    def is_filled(self):
        return self.filled
    
    def set_is_filled(self, filled):
        self.filled = filled

    @abc.abstractmethod
    def get_area(self) -> float:
        pass
        
    @abc.abstractmethod
    def get_perimeter(self) -> float:
        pass
        
    
class Circle(Shape):
    
    def __init__(self, radius, color='red', filled=True):
        Shape.__init__(self, color, filled)
        self.radius = radius
        
    def get_radius(self):
        return self._radius
    
    def set_radius(self, new_radius):
        self._radius = new_radius
        
    radius = property(get_radius, set_radius)
        
    def get_area(self):
        return math.pi * self.radius ^ 2
    
    def get_perimeter(self) -> float:
        return math.pi * self.radius * 2
    
    
class Rectangle(Shape):
    
    def __init__(self, width, length, color="red", filled=True):
        super().__init__(color, filled)
        self.length = length
        self.width = width

    def get_width(self):
        return self._width
    
    def set_width(self, new_width):
        self._width = new_width
        
    def get_length(self):
        return self._length
    
    def set_length(self, new_length):
        self._length = new_length

    length = property(get_length, set_length)
    width = property(get_width, set_width)
        
    def get_area(self):
        return self.width * self.length
    
    def get_perimeter(self):
        return 2 * (self.width + self.length)
    
    
class Square(Rectangle):
    
    def __init__(self, side, color='red', filled=True):
        self.side = side
        super().__init__(self.side, self.side, color=color, filled=filled)

    def get_side(self):
        return self.side
