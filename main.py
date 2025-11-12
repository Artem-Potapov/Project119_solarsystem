import turtle as trtl
import time
import os
import math

from potapov_collections import BetterTurtle

script_directory: str = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") #we'll need this to not mess up image import


class Planet:
  def __init__(self, _turtle: BetterTurtle, _orbit: int, _orbit_speed: int, _main_color:str):
    self.turtle = _turtle
    self.orbit_radius = _orbit
    self.main_color = _main_color
    self.orbit_speed = _orbit_speed
    self.turtle.color(self.main_color)
  
  def orbit(self, speed: int|None=None, steps: int=3):
    spd = self.orbit_speed
    self.turtle.circle(self.orbit_radius, extent=spd, steps=steps)
    
class PlanetWithImage(Planet):
  def __init__(self, _turtle: BetterTurtle, _orbit: int, _orbit_speed: int, _main_color_or_images: list[str]|str, color: str="green"):
    self.turtle = _turtle
    self.orbit_radius = _orbit
    self.images = _main_color_or_images
    self.main_color = color
    self.orbit_speed = _orbit_speed
    self.orbit_extent = 0
    self.current_image = None
    self.turtle.color(self.main_color)
  
  def orbit(self, speed: int|None=None, steps: int=3):
    spd = self.orbit_speed
    self.orbit_extent = (self.orbit_extent + spd) % 360
    if self.orbit_extent <= 90: 
      if self.current_image != self.images[0]: #so it doesn't constantly reload the same image which creates lag
        self.turtle.shape(self.images[0])
        self.current_image = self.images[0]
    elif self.orbit_extent <= 180:
      if self.current_image != self.images[1]:
        self.turtle.shape(self.images[1])
        self.current_image = self.images[1]
    elif self.orbit_extent <= 270:
      if self.current_image != self.images[2]:
        self.turtle.shape(self.images[2])
        self.current_image = self.images[2]
    elif self.orbit_extent <= 360:
      if self.current_image != self.images[3]:
        self.turtle.shape(self.images[3])
        self.current_image = self.images[3]
    self.turtle.circle(self.orbit_radius, extent=spd, steps=steps)
    
    

#init screen
app = trtl.Screen()
app.bgcolor("#110133")
for poser in range(1, 5):
  app.addshape(f"{script_directory}/earth{poser}.gif")
  app.addshape(f"{script_directory}/mars{poser}.gif")


#init sun
sun = BetterTurtle(shape="circle")
sun.color("yellow")
sun.turtlesize(7)

colors_or_images = ["brown", 
                    "#EE00EE", 
                    [[f"{script_directory}/earth{i}.gif" for i in range(1,5)], "green"], 
                    [[f"{script_directory}/mars{i}.gif" for i in range(1,5)], "orange"]]
sizes = [1.4, 2.5, 2.6, 2]
orbit_speeds = [15, 5, 6, 10]
positions = [140, 240, 340, -440]

planets = []
for col, size, poser, spd in zip(colors_or_images, sizes, positions, orbit_speeds):
  planet_turtle = BetterTurtle(start_pos=(poser, 0), shape="circle")
  planet_turtle.speed(0)
  planet_turtle.turtlesize(size)
  planet_turtle.setheading(90)
  if isinstance(col, (list, tuple)):
    planet = PlanetWithImage(planet_turtle, poser, spd, col[0], col[1])
  else:
    planet = Planet(planet_turtle, (poser), spd, col)
  planets.append(planet)


while True:
  for planet in planets:
    planet.orbit()
    


app.mainloop()