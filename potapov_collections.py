import turtle as trtl
import math

from typing import overload
from collections.abc import Sequence, MutableSequence
from abc import ABC, abstractmethod

class BetterTurtle(trtl.Turtle):
  def __init__(self, start_pos: Sequence = (0,0), shape = "classic", undobuffersize = 1000, visible = True):
    super().__init__(shape, undobuffersize, visible)
    if start_pos:
      self.pu()
      self._goto(trtl.Vec2D(start_pos[0], start_pos[1]))
      self.pd()
  # One thing that I love about OOP: you can just make a subclass of a class you want to fix,
  # and everything still works because polymorphism!
  @overload
  def goto(self, x: tuple[float, float], y: None = None, *, pu: bool = False, nor: bool = False) -> None: ...
  @overload
  def goto(self, x: float, y: float, *, pu: bool = False, nor: bool = False) -> None: ...

  def goto(self, x, y = None, *, pu: bool = False, nor: bool = False):
    # one thing that I hate is that turtle doesn't rotate in needed direction
    if isinstance(x, Sequence):
      x, y = x[0], x[1]
    if not nor:
      self.setheading(math.degrees(math.atan2(y - self._y, x - self._x))/self._degreesPerAU) # but now I fixed it :D
    if pu:
      self.pu()
    self._goto(trtl.Vec2D(x, y))
    if pu:
      self.pd()

  #Also, I like properties, getters, but they feel like attributes!
  @property
  def _y(self):
    return self.ycor()
  
  @property
  def _x(self):
    return self.xcor()
  
  @overload
  def rect(self, /, x1, y1, x0=None, y0=None ,*,
            color: str = None, thickness: int = None, fill: bool = False, fill_color: str = ""): ...

  @overload
  def rect(self, /, x0, y0, x1, y1 ,*,
            color: str = None, thickness: int = None, fill: bool = False, fill_color: str = ""): ...

  def rect(self, /, x0: int, y0: int, x1: int=None, y1: int=None, *,
            color: str = None, thickness: int = None, fill: bool = False, fill_color: str = ""):
    if color:
      self.color(color)
    if thickness:
      self.pensize(thickness)
    if (int(x1 is None) + int(y1 is None)) % 2 != 0:
      raise ValueError
    if x1 is None:
      x0, x1 = self._x, x0
    if y1 is None:
      y0, y1 = self._y, y0

    self.pu()
    self.goto(x0, y0)
    self.pd()

    if fill:
      self.begin_fill()
    if fill_color:
      self.fillcolor(fill_color)
    self.goto(x0, y1)
    self.goto(x1, y1)
    self.goto(x1, y0)
    self.goto(x0, y0)
    if fill:
      self.end_fill()

    self.pu()
    self.goto(x0, y0)
    self.pd()

    if fill:
      self.begin_fill()
    if fill_color:
      self.fillcolor(fill_color)
    self.goto(x0, y1)
    self.goto(x1, y1)
    self.goto(x1, y0)
    self.goto(x0, y0)
    if fill:
      self.end_fill()

  def poly(self, *points: Sequence[int], color: str=None, fill:bool=False):
    if color:
      self.color(color)
      self.pu()
      self.goto(points[0])
      self.pd()
    if fill:
      self.begin_fill()
    for point in points:
      self.goto(point)
    if fill:
      self.end_fill()

  def better_circle(self, radius: int, *, color=None, thickness: int=None, extent: float=None, steps: int=None, fill: bool = False, orientation: float= None):
    undocolor = self.color()
    undothickness = self.pensize()
    if orientation is not None:
      self.setheading(orientation)
    if color is not None:
      self.color(color)
    if thickness is not None:
      self.pensize(thickness)
    if fill:
      self.begin_fill()
    self.circle(radius, (extent if extent else None), (steps if steps else None))
    if fill:
      self.end_fill()
    self.color(undocolor[0])
    self.pensize(undothickness)

  def SUPERSONICSPEED(self):
    self.speed(0)
  
  def turtlespeed(self):
    self.speed(1)

class ABCFraction(ABC):
  @abstractmethod
  def simplify():
    ...
  
  @abstractmethod
  def _simplify():
    ...

class ABCRoot(ABC):
  @abstractmethod
  def simplify():
    ...
  
  @abstractmethod
  def _simplify():
    ...

class ABCNumber(ABC):
  @abstractmethod
  def _simplify():
    ...

  @abstractmethod
  def simplify():
    ...

class ABCNomial(ABCNumber):
  @abstractmethod
  def _simplify():
    ...

  @abstractmethod
  def simplify():
    ...

class ImmutableDict(dict):
  #A immutable dict.
  def __setitem__(self, key, value):
    raise RuntimeError("Trying to change immutable dict, make a copy")
  
  def __delitem__(self, key):
    raise RuntimeError("Trying to change immutable dict, make a copy")
  
  def __delattr__(self, name):
    raise RuntimeError("Trying to change immutable dict, make a copy")