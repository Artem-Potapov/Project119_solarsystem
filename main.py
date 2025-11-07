import turtle as trtl
import time
import os
import math

from potapov_collections import BetterTurtle

script_directory: str = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") #we'll need this to not mess up image import


class Planet:
  def __init__(self, _turtle: BetterTurtle, _orbit: int, _orbit_speed: int, _main_color_or_images: list[str]|str):
    self.turtle = _turtle
    self.orbit_radius = _orbit
    if isinstance(_main_color_or_images, list):
      self.images = _main_color_or_images
      self.main_color = "orange"
    else:
      self.main_color = _main_color_or_images
      self.turtle.color(self.main_color)
      self.images = []
    self.orbit_speed = _orbit_speed
  
  def orbit(self, speed: int|None=None, steps: int=3):
    if speed is not None:
      spd = speed
    else:
      spd = self.orbit_speed
    self.turtle.circle(self.orbit_radius, extent=spd, steps=steps)
    

#init screen
app = trtl.Screen()
app.bgcolor("#110133")
for i in range(1, 5):
  app.addshape(f"{script_directory}/earth{i}.gif")


#init sun
sun = BetterTurtle(shape="circle")
sun.color("yellow")
sun.turtlesize(7)

colors_or_images = ["brown", "#EE00EE", ["earth1"], "orange"]
sizes = [1.4, 2.5, 2.6, 2]
orbit_speeds = [3, 5, 6, 10]

planets = []
for col, size, i, spd in zip(colors_or_images, sizes, range(1, 5), orbit_speeds):
  planet_turtle = BetterTurtle(start_pos=(i*100+40, 0), shape="circle")
  planet_turtle.speed(0)
  planet_turtle.turtlesize(size)
  planet_turtle.setheading(90)
  planet = Planet(planet_turtle, i*100+40, spd, col)
  planets.append(planet)


while True:
  for planet in planets:
    planet.orbit()
    


app.mainloop()